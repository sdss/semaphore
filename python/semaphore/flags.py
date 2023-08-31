import numpy as np
from typing import Union, Optional, Tuple, Iterable

BitResolvable = Union[int, str]

class Flags:

    """An extensible mutable set of flags."""

    def __init__(
        self, 
        data: Optional[Union[bytearray, str, int, Iterable[BitResolvable]]] = None,
        reference=None
    ) -> None:
        """
        Initialize a new Flags object.
        
        :param data:
            The initial data to set the flags to. Can be a bytearray, a hex string, an integer, or an iterable of bits.
        
        :param reference: [optional]
            A reference to use when interpreting bits as strings.
        """
        
        self.reference = reference

        if data is not None:
            if isinstance(data, bytearray):
                self.data = data
            elif isinstance(data, str):
                self.data = bytearray.fromhex(data)
            elif isinstance(data, int):
                self.data = bytearray()
                self.set_bit(data)
            else:
                self.data = bytearray()
                for bit in data:
                    self.set_bit(bit)
        else:
            self.data = bytearray()

        return None
    
    
    @property
    def bits(self):
        """Return a tuple of all bits that are set."""
        bit, bits, size = (0, [], len(self.data))
        while True:
            num, offset = divmod(bit, 8)
            if num >= size:
                break
            if bool(self.data[num] & (1 << offset)):
                bits.append(bit)
            bit += 1
        return tuple(bits)

    
    @property
    def flags(self):
        """Return a tuple of all flag names that are set."""
        if self.reference is None:
            raise ValueError("Cannot return flag names without a flag reference")
        return tuple(self.reference[bit] for bit in self.bits)


    def set_bit(self, bit: BitResolvable) -> None:
        """
        Set the given bit.
        
        :param bit:
            The bit to set. Can be an integer or a string (if a reference was given).
        """
        num, offset = self._ensure_length(bit)
        self.data[num] |= (1 << offset)


    def set_bits(self, *bits: Iterable[BitResolvable]) -> None:
        """
        Set the given bits.
        
        :param *bits:
            An iterable of bits to set.
        """
        for bit in bits:
            self.set_bit(bit)


    def clear_bit(self, bit: BitResolvable) -> None:
        """
        Clear the given bit.
        
        :param bit:
            The bit to clear. Can be an integer or a string (if a reference was given).
        """
        num, offset = self._ensure_length(bit)
        self.data[num] &= ~(1 << offset)


    def clear_bits(self, *bits: Iterable[BitResolvable]) -> None:
        """
        Clear the given bits.
        
        :param *bits:
            An iterable of bits to clear.
        """
        for bit in bits:
            self.clear_bit(bit)            


    def toggle_bit(self, bit: BitResolvable) -> bool:
        """
        Toggle the given bit.
        
        :param bit:
            The bit to toggle. Can be an integer or a string (if a reference was given).
        
        :returns:
            The new state of the bit.
        """
        num, offset = self._ensure_length(bit)
        self.data[num] ^= (1 << offset)
        return bool(self.data[num] & (1 << offset))


    def toggle_bits(self, *bits: BitResolvable) -> None:
        """
        Toggle the given bits.
        
        :param *bits:
            An iterable of bits to toggle.
        """
        for bit in bits:
            self.toggle_bit(bit)
        return None
            

    def is_set(self, bit: BitResolvable) -> bool:
        """
        Return True if the given bit is set.
        
        :param bit:
            The bit to check. Can be an integer or a string (if a reference was given).
        """
        num, offset = self._ensure_length(bit)
        return bool(self.data[num] & (1 << offset))
    

    def are_any_set(self, *bits: Iterable[BitResolvable]) -> bool:
        """
        Return True if any given bits are set.
    
        :param *bits:
            An iterable of bits to check.
        """
        return any(self.is_set(bit) for bit in bits)
    

    def are_all_set(self, *bits: Iterable[BitResolvable]) -> bool:
        """
        Return True if all given bits are set.
        
        :param *bits:
            An iterable of bits to check.
        """
        return all(self.is_set(bit) for bit in bits)

    
    def len(self):
        return len(self.data)


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


    def _ensure_length(self, bit: BitResolvable) -> Tuple[int, int]:
        num, offset = divmod(self._resolve_bit_as_int(bit), 8)
        size = len(self.data)
        if size <= num:
            self.data.extend(b'\x00' * ((num + 1) - size))
        return (num, offset)


    def __repr__(self):
        return f"<{self.__class__.__name__} at {hex(id(self))}>"


    def __str__(self):
        return self.data.hex()
    

class FlagsArray:

    """An immutable flags array."""

    def __init__(
        self, 
        flags, #: Iterable[Union["Flags", BitResolvable]], 
        reference=None
    ) -> None:

        # TODO: Make this class mutable with some clever hacks

        # one giant bytearray, where each needs to be the same padded length to avoid index hell            
        if reference is None and isinstance(flags[0], Flags) and flags[0].reference is not None:
            self.reference = flags[0].reference
        else:
            self.reference = reference
        
        self._size = 0
        self._num_flags = len(flags)
        
        array_data = []
        for item in flags:
            if not isinstance(item, Flags):
                data = Flags(item).data
            else:
                data = item.data
            
            self._size = max(self._size, len(data))
            array_data.append(data)
        
        self.data = bytearray()
        for data in array_data:
            self.data.extend(data.ljust(self._size, b'\x00'))
        return None
    
    def __repr__(self):
        return f"<{self.__class__.__name__} with {self._num_flags} flags at {hex(id(self))}>"
    
    # TODO:
    # def bits, flags

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