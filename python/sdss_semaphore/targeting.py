import numpy as np
import os
import warnings
from typing import Union, Tuple, Iterable, Optional, List
from sdss_semaphore import BaseFlags, cached_class_property, logger
import importlib.resources as resources

class BaseTargetingFlags(BaseFlags):

    """A base class for communicating SDSS-V targeting information with flags."""

    @property
    def all_mappers(self) -> Tuple[str]:
        """Return a tuple of all mappers."""
        return self._all_attributes("mapper")
    
    @property
    def all_programs(self) -> Tuple[str]:
        """Return a list of all programs."""
        return self._all_attributes("program")
    
    @property
    def all_carton_names(self) -> Tuple[str]:
        """Return a list of all carton names."""
        return self._all_attributes("name")
    
    @property
    def all_alt_carton_names(self) -> Tuple[str]:
        """Return a list of all alternative carton names."""
        return self._all_attributes("alt_name")

    @property
    def all_alt_programs(self) -> Tuple[str]:
        """Return a list of all alternative carton programs."""
        return self._all_attributes("alt_program")
    
    def in_carton_label(self, label: str) -> np.array:
        """
        Return a N-length boolean array indicating whether the items are assigned to the carton with the given label.
        
        :param label:
            The carton label.
        """
        return self.is_attribute_set("label", label)

    def in_carton_pk(self, carton_pk: int) -> np.array:
        """
        Return an N-length boolean array indicating whether the items are assigned to the carton with the given primary key.

        :param carton_pk:
            The carton primary key.            
        """
        return self.is_attribute_set("carton_pk", carton_pk)

    def in_carton_name(self, name: str) -> np.array:
        """
        Return an N-length boolean array indicating whether the items are assigned to a carton with the given name.
        
        :param name:
            The flag name.
        """
        return self.is_attribute_set("name", name)

    def in_mapper(self, mapper: str) -> np.array:
        """
        Return an N-length boolean array indicating whether the items are assigned to any cartons with the given mapper.
        
        :param mapper:
            The mapper name.
        """
        return self.is_attribute_set("mapper", mapper)

    def in_program(self, program: str) -> np.array:
        """
        Return an N-length boolean array indicating whether the items are assigned to any cartons with the given program.
        
        :param program:
            The program name.
        """
        return self.is_attribute_set("program", program)
    
    def in_alt_name(self, alt_name: str) -> np.array:
        """
        Return an N-length boolean array indicating whether the items are assigned to any cartons with the given alternative name.

        :param alt_name:
            The alternative flag name.
        """
        return self.is_attribute_set("alt_name", alt_name)        

    def in_alt_program(self, alt_program: str) -> np.array:
        """
        Return an N-length boolean array indicating whether the items are assigned to any cartons with the given alternative program.

        :param alt_program:
            The alternative program name.
        """
        return self.is_attribute_set("alt_program", alt_program)

    def get_carton_pk(self, index: int = None) -> Tuple[str]:
        """
        Returns the Tuple of list of carton pks for a target
        If a list or numpy array of indices is provided, it returns a list of 1-element Tuples,
            each matching the corresponding index.

        :param index:
            The index of the Target in the TargetingFlag array
        """
        return self.get_attribute("carton_pk", index)

    def get_carton_label(self, index: Union[int, List[int], np.ndarray] = None) -> Tuple[str]:
        """
        Returns the Tuple of list of carton cables for a target
        If an index is provided it returns a 1-element Tuple matching that index
        If a list or numpy array of indices is provided, it returns a list of 1-element Tuples,
            each matching the corresponding index.

        :param index:
            The index or indices of the Target in the TargetingFlag array
        """
        
        return self.get_attribute("label", index)

    def get_carton_name(self, index: int = None) -> Tuple[str]:
        """
        Returns the Tuple of list of cartons names for a target
        If an index is provided it returns a 1-element Tuple matching that index
        If a list or numpy array of indices is provided, it returns a list of 1-element Tuples,
            each matching the corresponding index.

        :param index:
            The index of the Target in the TargetingFlag array
        """
        return self.get_attribute("name", index)

    def get_mapper(self, index: int = None) -> Tuple[str]:
        """
        Returns the Tuple of list of mappers for a target
        If an index is provided it returns a 1-element Tuple matching that index
        If a list or numpy array of indices is provided, it returns a list of 1-element Tuples,
            each matching the corresponding index.

        :param index:
            The index of the Target in the TargetingFlag array
        """
        return self.get_attribute("mapper", index)

    def get_program(self, index: int = None) -> Tuple[str]:
        """
        Returns the Tuple of list of alt_program for a target
        If an index is provided it returns a 1-element Tuple matching that index
        If a list or numpy array of indices is provided, it returns a list of 1-element Tuples,
            each matching the corresponding index.

        :param index:
            The index of the Target in the TargetingFlag array
        """
        return self.get_attribute("program", index)
        
    def get_alt_name(self, index: int = None) -> Tuple[str]:
        """
        Returns the Tuple of list of alt_name for a target
        If an index is provided it returns a 1-element Tuple matching that index
        If a list or numpy array of indices is provided, it returns a list of 1-element Tuples,
            each matching the corresponding index.

        :param index:
            The index of the Target in the TargetingFlag array
        """
        return self.get_attribute("alt_name", index)

    def get_alt_program(self, index: int = None) -> Tuple[str]:
        """
        Returns the Tuple of list of alt_program for a target
        If an index is provided it returns a 1-element Tuple matching that index
        If a list or numpy array of indices is provided, it returns a list of 1-element Tuples,
            each matching the corresponding index.

        :param index:
            The index of the Target in the TargetingFlag array
        """
        return self.get_attribute("alt_program", index)

    def count(self, skip_empty: bool = False) -> dict:
        """
        Return a dictionary containing the number of items assigned by each carton label.

        :param skip_empty: [optional]
            Skip cartons with no items assigned to them.
        
        :returns:
            A dictionary with carton labels as keys and item counts as values.
        """
        return self._count(
            { attrs["label"]: [bit] for bit, attrs in self.mapping.items() }, 
            skip_empty=skip_empty
        )

    def set_bit_by_carton_pk(self, index: int, carton_pk: int):
        """
        Set the bit for the carton with the given primary key.

        :param index:
            The index of the item to set.

        :param carton_pk:
            The carton primary key.        
        """
        bit = self.bit_position_from_carton_pk[carton_pk]
        return self.set_bit(index, bit)

    @cached_class_property
    def bit_position_from_carton_pk(self):
        """
        Return a dictionary with carton primary keys as keys, and bit positions as values.
        
        This is a helper method for efficiency creating large `TargetingFlags` objects.
        """
        return { attrs["carton_pk"]: bit for bit, attrs in self.mapping.items() }

    @cached_class_property
    def version(self):
        raise NotImplementedError(f"`version` must be defined in subclass")
        
    @cached_class_property
    def _ver_name(self):
        raise NotImplementedError(f"`ver_name` must be defined in subclass")

    @cached_class_property
    def _MAPPING_BASENAME(self):
        raise NotImplementedError(f"`_MAPPING_BASENAME` must be defined in subclass")

    @classmethod
    def set_version(cls, version: int):
        """Set the SDSSC2BV value and reload the mapping."""
        if getattr(cls, "version", None) == version and hasattr(cls, "_mapping_"):
            # If the version matches the current one and the mapping is cached, do nothing
            return
        
        MAPPING_BASENAME = cls._MAPPING_BASENAME.format(version = version)
        try: #python 3.9+
            path = resources.files(__name__.split('.')[0]).joinpath('etc',f'{MAPPING_BASENAME}')
        except: #python 3.7,3.8
            try:
                with resources.path(__name__.split('.')[0]+'.etc', f'{MAPPING_BASENAME}') as path:
                    path = str(path)
            except FileNotFoundError:
                path = ''

            
        if not os.path.exists(path):
            warnings.warn(
                f"{cls._ver_name} = {version} is invalid, defaulting to {cls._ver_name} = {cls.version}",
                InvalidVersionWarning)
            cls.MAPPING_BASENAME = cls._MAPPING_BASENAME.format(version = cls.version)
            return
 
        logger.debug(f"Using {cls._ver_name}={version} from {path}")
        cls.version = version
        cls.MAPPING_PATH = os.path.dirname(path)
        cls.MAPPING_BASENAME = MAPPING_BASENAME

        # Clear the cached mapping so it will be reloaded
        if hasattr(cls, '_mapping_'):
            del cls._mapping_

class InvalidVersionWarning(Warning):
    """Custom warning for invalid version values."""
    pass

class TargetingFlags(BaseTargetingFlags):

    """Communicating with SDSS-V targeting flags."""

    dtype, n_bits = (np.uint8, 8)
    version = 3
    _ver_name = 'SDSSC2BV'
    _MAPPING_BASENAME = "sdss5_target_{version}_with_groups.csv"
        
    # TODO: Metadata about mapping version should be stored in the MAPPING_BASENAME file
    #       and be assigned as a cached class property once the file is loaded.
    
    # TODO: Update this file once we have finalised the format and content.

    def __init__(self,
                 array: Optional[Union[np.ndarray, Iterable[Iterable[int]],
                                 Iterable[bytearray], Iterable['BaseFlags']]] = None, #Flag array
                 sdssc2bv: Optional[int] = None, #manually set the Carton to bit version
                 *params,  # *params for extra (unexpected) positional arguments
                 **kwargs  # **kwargs for extra (unexpected) keyword arguments
                 ) -> None:
        """Initialize TargetingFlags with an optional sdssc2bv value."""
        if sdssc2bv is None:
            sdssc2bv = int(os.getenv('SDSSC2BV', default=self.version))
        self.set_version(sdssc2bv)
        super().__init__(array)
