import numpy as np
from typing import Union, Optional, Tuple, Iterable

from semaphore.flags import Flags
from semaphore.reference import FlagsReference

class FlagsArray:

    """An extensible representation of an array of mutable flags."""

    def __init__(
        self, 
        data: Union[np.ndarray, Iterable[Flags]], 
        reference: Optional[FlagsReference] = None
    ) -> None:
        """
        Initialize a new FlagsArray object.
        
        :param data:
            An iterable of ``Flags`` objects, or a Numpy array of integers that encode the flags.
        
        :param reference: [optional]
            A reference to use when resolving flag names to bit positions.
        """

        if (
            (data is not None)
        and (not isinstance(data, np.ndarray))
        and (not isinstance(data, Iterable) or not all(isinstance(item, Flags) for item in data))
        ):
            raise TypeError(f"`data` must be an iterable of `Flags` objects or a numpy array not {type(data)}")

        # If no reference is given, use the first one we can find.
        self.reference = reference
        if self.reference is None and not isinstance(item, np.ndarray):
            for item in data:
                if item.reference is not None:
                    self.reference = item.reference
                    break

        if isinstance(data, np.ndarray):
            self.data = np.atleast_2d(data.copy(), dtype=np.uint8)
        else:
            N, F = (len(data), max(len(item) for item in data))
            self.data = np.zeros((N, F), dtype=np.uint8)
            for i, item in enumerate(data):
                self.data[i, :len(item)] = item.array
        return None
        

    def get_bits(self, index):
        """
        Return a tuple of bits that are set for the given index.
        
        :param index:
            The index to get the bits for.
        """
        bit, bits, size = (0, [], self.data.shape[1])
        while True:
            num, offset = divmod(bit, 8)
            if num >= size:
                break
            if bool(self.data[index, num] & (1 << offset)):
                bits.append(bit)
            bit += 1
        return tuple(bits)

    
    def get_flags(self, index):
        """
        Return a tuple of all flag names that are set for the given index.
        
        :param index:
            The index to get the flag names for.
        """
        if self.reference is None:
            raise ValueError("Cannot return flag names without a flag reference")
        return tuple(self.reference[bit] for bit in self.get_bits(index))
    

    def get_bit_position(self, flag: str) -> int:
        """
        Get the bit position for the given flag.
        
        This does not return whether the flag is set or not. It only returns the position.

        :param flag:
            The flag to get the bit position for.
        
        :raises ValueError:
            If no reference exists.

        :raises KeyError:
            If the flag is not found in the reference.

        :returns:
            The bit position for the given flag.
        """
        try:
            bit = self.reference[flag]
        except:
            if self.reference is None:
                raise ValueError("Cannot interpret bit as string without flag reference")
            else:
                raise KeyError(f"Cannot interpret flag '{flag}' from reference")     
        return bit


    def is_bit_set(self, bit: int) -> np.array:
        """
        Return a boolean array indicating whether the given bit is set for each item.

        :param bit:
            The bit to check.
        """
        num, offset = self._get_num_and_offset(bit)
        N, F = self.data.shape
        if F > num:
            return (self.data[:, num] & (1 << offset)).astype(bool)
        else:
            return np.zeros(N, dtype=bool)


    def is_flag_set(self, flag: str) -> np.array:
        """
        Return a boolean array indicating whether the given flag is set for each item.

        :param flag:
            The flag to check.
        """
        return self.is_bit_set(self.get_bit_position(flag))


    def set_bit(self, index, bit):
        """
        Set the given bit for the given index.
        
        :param index:
            The index to set the bit for.
        
        :param bit:
            The bit to set.
        """
        num, offset = self._ensure_shape_for_bit(bit)
        self.data[index, num] |= (1 << offset)
        return self


    def set_flag(self, index, flag):
        """
        Set the given flag for the given index.
        
        :param index:
            The index to set the flag for.

        :param flag:
            The flag to set.
        """
        return self.set_bit(index, self.get_bit_position(flag))


    def clear_bit(self, index, bit):
        """
        Clear the given bit for the given index.
        
        :param index:
            The index to clear the bit for.
            
        :param bit:
            The bit to clear.
        """
        num, offset = self._ensure_shape_for_bit(bit)
        self.data[index, num] &= ~(1 << offset)
        return self
    

    def clear_flag(self, index, flag):
        """
        Clear the given flag for the given index.
        
        :param index:
            The index to clear the flag for.
            
        :param flag:
            The flag to clear.
        """
        return self.clear_bit(index, self.get_bit_position(flag))
    

    def toggle_bit(self, index, bit):
        """
        Toggle the given bit for the given index.
        
        :param index:
            The index to toggle the bit for.
        
        :param bit:
            The bit to toggle.
        """
        num, offset = self._ensure_shape_for_bit(bit)
        self.data[index, num] ^= (1 << offset)
        return self
    

    def toggle_flag(self, index, flag):
        """
        Toggle the given flag for the given index.
        
        :param index:
            The index to toggle the flag for.
        
        :param flag:
            The flag to toggle.
        """
        return self.toggle_bit(index, self.get_bit_position(flag))
    

    def shrink(self):
        """Shrink the data array to the maximum required shape based on the highest bit set."""
        index = 1 + np.where(np.any(self.data > 0, axis=0))[0][-1]
        self.data = self.data[:, :index]
        return self
    

    def to_fits_column(self, name, shrink=True, **kwargs):
        """
        Return a FITS column object for this array.
        
        :param name:
            The name of the column.
        
        :param shrink: [optional]
            If `True`, shrink the array to the minimum required size before writing.
        """
        from astropy.io import fits

        if shrink:
            self.shrink()
        
        N, F = self.data.shape
        return fits.Column(
            name=name,
            array=self.data,
            format=f"{F}B",
            dim=f"({F})",
            **kwargs
        )


    def _stack_is_bit_set(self, *bits: Iterable[int]) -> np.array:
        # TODO: this could be vectorized
        return np.vstack([self.is_bit_set(bit) for bit in bits])

    def are_any_bits_set(self, *bits: Iterable[int]) -> np.array:
        return self._stack_is_bit_set(*bits).any(axis=0)

    def are_all_bits_set(self, *bits: Iterable[int]) -> np.array:
        return self._stack_is_bit_set(*bits).all(axis=0)

    def are_any_flags_set(self, *flags: Iterable[str]) -> np.array:
        return self._stack_is_bit_set(*map(self.get_bit_position, flags)).any(axis=0)

    def are_all_flags_set(self, *flags: Iterable[str]) -> np.array:
        return self._stack_is_bit_set(*map(self.get_bit_position, flags)).all(axis=0)

    def _get_num_and_offset(self, bit):
        return divmod(bit, 8)

    def _ensure_shape_for_bit(self, bit: int) -> Tuple[int, int]:
        num, offset = divmod(bit, 8)
        N, F = self.data.shape
        if F <= num:
            C = (num + 1) - F
            # little-endian
            self.data = np.hstack([
                self.data,
                np.zeros((N, C), dtype=self.data.dtype)
            ])
        return (num, offset)

    def __repr__(self):
        return f"<{self.__class__.__name__} with shape {self.data.shape} at {hex(id(self))}>"