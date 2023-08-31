from typing import Union, Optional, Tuple, Iterable
from types import BitResolvable


class Flags:

    def __init__(
        self, 
        data: Optional[Union[bytearray, str, int, Iterable[BitResolvable]]] = None,
        reference=None
    ) -> None:
        
        self.reference = reference

        if data is not None:
            if isinstance(data, bytearray):
                self.data = data
            elif isinstance(data, str):
                self.data = bytearray.fromhex(data)
            elif isinstance(data, int):
                self.data = bytearray()
                self.set_bit(int)
            else:
                self.data = bytearray()
                for bit in data:
                    self.set_bit(bit)
        else:
            self.data = bytearray()

        return None
    
    
    @property
    def bits(self):
        bit, bits, size = (0, [], len(self.data))
        while True:
            num, offset = divmod(bit, 8)
            if num >= size:
                break
            if bool(self.data[num] & (1 << offset)):
                bits.append(bit)
            bit += 1
        return tuple(bits)

            
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


    def set_bit(self, bit: BitResolvable) -> None:
        num, offset = self._ensure_length(bit)
        self.data[num] |= (1 << offset)


    def set_bits(self, *bits: Iterable[BitResolvable]) -> None:
        for bit in bits:
            self.set_bit(bit)


    def clear_bit(self, bit: BitResolvable) -> None:
        num, offset = self._ensure_length(bit)
        self.data[num] &= ~(1 << offset)


    def clear_bits(self, *bits: Iterable[BitResolvable]) -> None:
        for bit in bits:
            self.clear_bit(bit)            


    def toggle_bit(self, bit: BitResolvable) -> bool:
        num, offset = self._ensure_length(bit)
        self.data[num] ^= (1 << offset)
        return bool(self.data[num] & (1 << offset))


    def toggle_bits(self, *bits: BitResolvable) -> bool:
        for bit in bits:
            self.toggle_bit(bit)
            

    def is_set(self, bit: BitResolvable) -> bool:
        num, offset = self._ensure_length(bit)
        return bool(self.data[num] & (1 << offset))
    

    def are_any_set(self, *bits: Iterable[BitResolvable]) -> bool:
        return any(self.is_set(bit) for bit in bits)
    

    def are_all_set(self, *bits: Iterable[BitResolvable]) -> bool:
        return all(self.is_set(bit) for bit in bits)


    def __repr__(self):
        return f"<{self.__class__.__name__} at {hex(id(self))}>"


    def __str__(self):
        return self.data.hex()
    


class FlagsArray:

    def __init__(self, flags: Iterable[Union[Flags, BitResolvable]], reference=None) -> None:
        self.reference = reference

        # one giant bytearray, where each needs to be the same padded length to avoid index hell
