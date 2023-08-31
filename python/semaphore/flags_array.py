import numpy as np
from typing import Union, Optional, Tuple, Iterable
#from types import BitResolvable
BitResolvable = Union[int, str]


class FlagsArray:

    """
    An immutable flags array.
    """

    def __init__(
        self, 
        flags, #: Iterable[Union["Flags", BitResolvable]], 
        reference=None
    ) -> None:
        self.reference = reference

        # one giant bytearray, where each needs to be the same padded length to avoid index hell
        self._size = max(len(flag.data) for flag in flags)
        self.data = bytearray()
        for flag in flags:
            self.data.extend(flag.data.ljust(self._size, b'\x00'))

        return None
    

    def is_set(self, bit: BitResolvable) -> bool:
        num, offset = divmod(self._resolve_bit_as_int(bit), 8)
        return (np.array(self.data[num::self._size]) & (1 << offset)).astype(bool)


    def are_any_set(self, *bits: Iterable[BitResolvable]) -> np.array:
        return self._op_is_set(np.any, *bits)


    def are_all_set(self, *bits: Iterable[BitResolvable]) -> np.array:
        return self._op_is_set(np.all, *bits)


    def sum_set(self, *bits: Iterable[BitResolvable]) -> np.array:
        return self._op_is_set(np.sum, *bits)


    def _op_is_set(self, op, *bits: Iterable[BitResolvable]) -> np.array:
        return op(np.vstack([self.is_set(bit) for bit in bits]), axis=0)


    def _resolve_bit_as_int(self, bit: BitResolvable):
        if isinstance(bit, int):
            return bit
        else:
            try:
                return self.reference[bit]
            except:
                if self.reference is None:
                    raise ValueError("Cannot interpret bit as string without flag reference")
                else:
                    raise ValueError(f"Cannot interpret bit '{bit}' from reference")                


    #def _ensure_length(self, bit: BitResolvable) -> Tuple[int, int]:
    #    num, offset = divmod(self._resolve_bit_as_int(bit), 8)
    #    size = len(self.data)
    #    if size <= num:
    #        self.data.extend(b'\x00' * ((num + 1) - size))
    #    return (num, offset)

