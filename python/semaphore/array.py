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
        if self.reference is None:
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
        

    def get_bit_index(self, flag: str) -> int:
        """
        Get the bit index for the given flag.
        
        This does not return whether the flag is set or not. It only returns the position.

        :param flag:
            The flag to get the bit index for.
        
        :raises ValueError:
            If no reference exists.

        :raises KeyError:
            If the flag is not found in the reference.

        :returns:
            The bit index for the given flag.
        """
        try:
            bit = self.reference[flag]
        except:
            if self.reference is None:
                raise ValueError("Cannot interpret bit as string without flag reference")
            else:
                raise KeyError(f"Cannot interpret flag '{flag}' from reference")     
        return bit


    def is_bit_set(self, bit: int):
        num, offset = self._get_num_and_offset(bit)
        N, F = self.data.shape
        if F > num:
            return (self.data[:, num] & (1 << offset)).astype(bool)
        else:
            return np.zeros(N, dtype=bool)


    def is_flag_set(self, flag: str):
        return self.is_bit_set(self.get_bit_index(flag))


    def set_bit(self, index, bit):
        num, offset = self._ensure_shape_for_bit(bit)
        self.data[index, num] |= (1 << offset)
        return self


    def set_flag(self, index, flag):
        return self.set_bit(index, self.get_bit_index(flag))


    def clear_bit(self, index, bit):
        num, offset = self._ensure_shape_for_bit(bit)
        self.data[index, num] &= ~(1 << offset)
        return self
    

    def clear_flag(self, index, flag):
        return self.clear_bit(index, self.get_bit_index(flag))
    

    def toggle_bit(self, index, bit):
        num, offset = self._ensure_shape_for_bit(bit)
        self.data[index, num] ^= (1 << offset)
        return self
    

    def toggle_flag(self, index, flag):
        return self.toggle_bit(index, self.get_bit_index(flag))
    

    def _stack_is_bit_set(self, *bits: Iterable[int]) -> np.array:
        # TODO: this could be vectorized
        return np.vstack([self.is_bit_set(bit) for bit in bits])

    def are_any_bits_set(self, *bits: Iterable[int]) -> np.array:
        return self._stack_is_bit_set(*bits).any(axis=0)

    def are_all_bits_set(self, *bits: Iterable[int]) -> np.array:
        return self._stack_is_bit_set(*bits).all(axis=0)

    def are_any_flags_set(self, *flags: Iterable[str]) -> np.array:
        return self._stack_is_bit_set(*map(self.get_bit_index, flags)).any(axis=0)

    def are_all_flags_set(self, *flags: Iterable[str]) -> np.array:
        return self._stack_is_bit_set(*map(self.get_bit_index, flags)).all(axis=0)

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

    # TODO: shrink() function to make array smaller (as small as biggest bit set)
    # 

    def __repr__(self):
        return f"<{self.__class__.__name__} with shape {self.data.shape} at {hex(id(self))}>"