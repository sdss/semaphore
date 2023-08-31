from typing import Union, Optional, Tuple, Iterable
#from types import BitResolvable
BitResolvable = Union[int, str]

class Flags:

    """
    A mutable set of flags.
    """

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