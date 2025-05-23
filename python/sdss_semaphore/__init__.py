__version__ = "0.2.7"

import numpy as np
import warnings
import os.path as ptt
from typing import Dict, Union, Tuple, Iterable, List, Optional, Tuple
import importlib.resources as resources
import logging


logger = logging.getLogger(__name__)
def setup_logging(level=logging.DEBUG):
    """Quickly configure logging for debugging purposes."""
    logging.basicConfig(level=level, format="%(asctime)s - %(name)s - %(funcName)s - %(levelname)s - %(message)s")


class cached_class_property:
    """
    Descriptor decorator implementing a class-level, read-only
    property, which caches its results on the class(es) on which it
    operates.

    From the Dicken's library
    """
    class AliasConflict(ValueError):
        pass

    def __init__(self, func):
        self.__func__ = func
        self.__cache_name__ = '_{}_'.format(func.__name__.strip('_'))
        if self.__cache_name__ == func.__name__:
            raise self.AliasConflict(self.__cache_name__)

    def __get__(self, instance, cls=None):
        if cls is None:
            cls = type(instance)

        try:
            return vars(cls)[self.__cache_name__]
        except KeyError:
            result = self.__func__(cls)
            setattr(cls, self.__cache_name__, result)
            return result


class BaseFlags:

    """A base class for communicating with flags."""

    def __init__(self, array: Optional[Union[np.ndarray, Iterable[Iterable[int]], Iterable[bytearray], Iterable['BaseFlags']]] = None) -> None:
        if array is None:
            # Assume single object flag.
            self.array = np.zeros((1, 0), dtype=self.dtype)
        elif isinstance(array, (list, tuple, np.ndarray)) and isinstance(array[0], (bytearray, str)):
            # TODO: If the self.dtype is not uint8, then we might need to compute these initial offsets ourselves,
            #       because I think bytearray is natively uint8
            if self.dtype != np.uint8:
                warnings.warn("Converting from list of bytearrays to integer array, but `dtype` is not uint8. Hold on to your butts.")
            if isinstance(array[0], str):
                logger.warning("Warning: Converting from string to bytearrays assuming string is hexadecimal")
                array = [bytes.fromhex(h) for h in np.atleast_1d(array)]
            N, F = (len(array), max(len(item) for item in array))
            self.array = np.zeros((N, F), dtype=self.dtype)
            for i, item in enumerate(array):
                self.array[i, :len(item)] = np.frombuffer(item, dtype=self.dtype)
        elif len(array) > 0 and isinstance(array[0], BaseFlags):
            # need to pad the array to the maximum size
            N, F, si = (0, 0, 0)
            for item in array:
                n, f = item.array.shape
                F = max(F, f)
                N += n
            self.array = np.zeros((N, F), dtype=self.dtype)
            for item in array:
                n, f = item.array.shape
                self.array[si:si + n, :f] = item.array
                si += n        
        elif isinstance(array, str):
            logger.warning("Warning: Converting from string to bytearrays assuming string is hexadecimal")
            array = [bytes.fromhex(h) for h in np.atleast_1d(array)]
            N, F = (len(array), max(len(item) for item in array))
            self.array = np.zeros((N, F), dtype=self.dtype)
            for i, item in enumerate(array):
                self.array[i, :len(item)] = np.frombuffer(item, dtype=self.dtype)
        else:
            self.array = np.atleast_2d(array).astype(self.dtype)
        return None

    def __getitem__(self, index: int):
        if isinstance(index, tuple):
            raise IndexError("too many indices for array; you can only slice on items")
        return self.__class__(self.array[[index]])

    @property
    def dtype(self):
        raise NotImplementedError(f"`dtype` must be defined in subclass")
    
    @property
    def n_bits(self):
        raise NotImplementedError(f"`n_bits` must be defined in subclass")

    @cached_class_property
    def MAPPING_PATH(self):
        raise NotImplementedError(f"`MAPPING_PATH` must be defined in subclass")

    @cached_class_property
    def MAPPING_BASENAME(self):
        raise NotImplementedError(f"`MAPPING_BASENAME` must be defined in subclass")

    @cached_class_property
    def mapping(self) -> dict:
        """A dictionary containing bit positions as keys, and dictionaries of flag attributes as values."""

        """Load and cache the mapping file."""
        if not hasattr(self, "MAPPING_PATH") or self.MAPPING_PATH is None:
            raise RuntimeError("Mapping path is not set. Call `set_version` first.")

        # TODO: The format and content of the mapping file is TBD. Here we will just load the CSV we have.
        #       Once we have finalized the format and content, move this import out and add dependency (fits/astropy).
        logger.debug('Reading: '+ptt.join(self.MAPPING_PATH, self.MAPPING_BASENAME))
        from astropy.table import Table
        mapping = {}
        for row in Table.read(ptt.join(self.MAPPING_PATH, self.MAPPING_BASENAME)):
            row_dict = dict(zip(row.colnames, row))
            mapping[row_dict["bit"]] = row_dict
        return mapping
            
    @property
    def bits_set(self) -> Iterable[Tuple[int]]:
        """
        A generator that yields a tuple of bits set for each item.
        
        If you want a more efficient lookup, you can use:

            items, bits = np.where(flags.as_boolean_array())
            
        """
        for row in self.as_boolean_array():
            yield tuple(np.where(row)[0])

    @property
    def flags_set(self) -> Iterable[Tuple[Dict]]:
        """
        A generator that yields all set flags.
        
        This can be a hugely expensive query if you have large number of items (e.g., stars).
        """
        for row in self.as_boolean_array():
            yield tuple(self.mapping[bit] for bit in np.where(row)[0])
        
    def _all_attributes(self, key):
        """Helper function to return unique set of attributes for all flags."""
        return tuple(set(attrs[key] for attrs in self.mapping.values()))

    def count(self, skip_empty: bool = False) -> dict:
        """
        Return a dictionary containing the number of items assigned with each flag.
        
        :param skip_empty: [optional]
            Skip flags with no items assigned to them.
        """
        return self._count(
            { bit: [bit] for bit in self.mapping.keys() }, 
            skip_empty=skip_empty
        )

    def count_by_attribute(self, attribute, skip_empty: bool = False) -> dict:
        """
        Return a dictionary of the items assigned with flags of a given attribute.

        The keys are the bit positions of each flag, or if an attribuet is given, then this will
        be the attribute of the flags to count. The values are the number of items assigned to 
        flags with that attribute.
    
        :param attribute:
            The flag attribute to count by.
        
        :param skip_empty: [optional]
            Skip flags with no items assigned to them.
        """    
        # Need bits per attribute to avoid double-counting
        bits_per_attribute = {}
        for bit, attributes in self.mapping.items():
            bits_per_attribute.setdefault(attributes[attribute], [])
            bits_per_attribute[attributes[attribute]].append(bit)
        return self._count(bits_per_attribute, skip_empty=skip_empty)

    def _count(self, bits_per_attribute, skip_empty: bool = False) -> dict:
        """
        Count the number of items assigned to flags with given attributes.

        :param bits_per_attribute:
            A dictionary of the bit positions for each attribute.
        
        :param skip_empty: [optional]
            Skip flags with no items assigned to them.        
        """        
        counts = {}
        for attribute, bits in bits_per_attribute.items():
            count = np.sum(self.are_any_bits_set(bits))
            if count > 0 or not skip_empty:
                counts[attribute] = count            
        return counts
        
    def as_boolean_array(self) -> np.ndarray:
        """
        Return a (N, F) shaped big-endian boolean array indicating whether each bit is set for 
        each item, where the input data array has shape (N, B) and `F = B * n_bits` is the maximum
        possible number of flags.
        """
        N, B = self.array.shape
        num, offset = np.divmod(np.arange(B * self.n_bits), self.n_bits)
        return (self.array[:, num] & (1 << offset)).astype(bool)

    def shrink(self):
        """Shrink the data array to the maximum required shape based on the highest bit set."""
        index = 1 + np.where(np.any(self.array > 0, axis=0))[0][-1]
        self.array = self.array[:, :index]
        return self

    def get_attribute(self, key, index: Union[int, List[int], np.ndarray] = None) -> Tuple:
        """
        Return a list of the set values for a key for a single target
        
        :param key:
            The attribute key.
        
        :param index:
            The index of the target in the Targeting Flag
        
        :returns:
            A list of the requested attibute for the stet flags
        """
        if index is None:
            _flags = self
        elif isinstance(index, (int, np.integer)):
            # Single index case
            _flags = self[index]
        elif isinstance(index, (list, np.ndarray)):
            _flags = [self[i] for i in index]
        elif isinstance(index, np.ndarray):
            _flags = [self[i] for i in index.tolist()]  # Convert numpy array to list and index
        else:
            raise TypeError("Index must be an int, a list of ints, or a numpy array of ints.")

        return tuple([[d[key] for d in t_of_d if key in d]
                      for _flag in _flags for t_of_d in _flag.flags_set])


        
    def is_attribute_set(self, key, value) -> np.array:
        """
        Return a N-length boolean array indicating whether the item has any flag with the given attribute.
        
        :param key:
            The attribute key.

        :param value:
            The attribute value.
        
        :returns:
            A boolean array indicating whether the item has any flag with the given attribute.
        """
        bits = self.get_bits_with_attribute(key, value)
        if len(bits) == 0:
            raise ValueError(f"No bits found with attribute {key}={value}")
        num, offset = np.divmod(bits, self.n_bits)
        N, B = self.array.shape
        can_be_set = B > num
        return np.any(self.array[:, num[can_be_set]] & (1 << offset[can_be_set]), axis=1)

    
    def get_bits_with_attribute(self, key, value) -> List[int]:
        """
        Return the bit positions for all items with the given attribute.
    
        :param key:
            The attribute key.
        
        :param value:
            The attribute value.
        
        :returns:
            A list of bit positions.
        """
        bits = []
        for bit, attrs in self.mapping.items():
            try:
                if attrs[key] == value:
                    bits.append(bit)
            except KeyError:
                continue
        return bits
    
    def are_any_bits_set(self, *bits) -> np.array:
        """
        Return an N-length boolean array indicating whether any of the given bits are set for each item.
    
        :param bits:
            The zero-indexed bit positions to check.
        
        :returns:
            A boolean array indicating whether any of the given bits are set for each item.
        """
        return np.any(self._check_bits(*bits), axis=1)
    
    def are_all_bits_set(self, *bits) -> np.array:
        """
        Return an N-length boolean array indicating whether all of the given bits are set for each item.
        
        :param bits:
            The zero-indexed bit positions to check.
        
        :returns:
            A boolean array indicating whether all of the given bits are set for each item.
        """
        return np.all(self._check_bits(*bits), axis=1)

    def is_bit_set(self, bit) -> np.array:
        """
        Return an N-length boolean array indicating whether the given bit is set for each item.

        :param bit:
            The zero-indexed bit position to check.
        
        :returns:
            A boolean array indicating whether the given bit is set for each item.
        """        
        return self.are_any_bits_set(bit)

    def set_bit(self, index, bit):
        """
        Set the given bit for the given item.
        
        :param index:
            The item index.
        
        :param bit:
            The zero-indexed bit position to set.
        """        
        num, offset = self._ensure_shape_for_bit(bit)        
        self.array[index, num] |= (1 << offset)
        return self

    def clear_bit(self, index, bit):
        """
        Clear the given bit for the given index.
        
        :param index:
            The item index.
            
        :param bit:
            The zero-indexed bit position to clear.
        """
        # Here we don't ensure_shape_for_bit because we don't want to create a YUGE array just
        # to clear a ficticious bit at position 2**128
        num, offset = np.divmod(bit, self.n_bits)
        N, B = self.array.shape
        is_set_able = B > num
        offset = offset[is_set_able]
        mask = ~(np.left_shift(1, offset)).astype(self.dtype)
        self.array[index, num] &= mask
        return self
    
    def toggle_bit(self, index, bit):
        """
        Toggle the given bit for the given index.
        
        :param index:
            The item index.
            
        :param bit:
            The zero-indexed bit position to clear.
        """
        num, offset = self._ensure_shape_for_bit(bit)
        self.array[index, num] ^= (1 << offset)
        return self
        
    def _check_bits(self, *bits):
        """Check whether the given bits are set or not."""
        num, offset = np.divmod(bits, self.n_bits)
        N, B = self.array.shape
        can_be_set = B > num
        return self.array[:, num[can_be_set]] & (1 << offset[can_be_set])

    def _ensure_shape_for_bit(self, bit: int) -> Tuple[int, int]:
        """
        Ensure the data array has sufficient size to store information about the given bit.
        
        :param bit:
            The zero-indexed bit position to check.
        
        :returns:
            A tuple of the number of the data array column and the bit offset within that column.
        """
        num, offset = np.divmod(bit, self.n_bits)
        N, F = self.array.shape
        if F <= np.max(num):
            C = (np.max(num) + 1) - F
            # little-endian
            self.array = np.hstack([
                self.array,
                np.zeros((N, C), dtype=self.array.dtype)
            ])
        return (num, offset)

    def __repr__(self):
        N, B = self.array.shape
        return f"<{self.__class__.__name__} with {N:,} items and up to {B * self.n_bits:,} flags ({len(self.mapping):,} defined) at {hex(id(self))}>"

    def __len__(self):
        N, B = self.array.shape
        return N
