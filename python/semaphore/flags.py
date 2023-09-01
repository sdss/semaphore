import numpy as np
from typing import Optional, Tuple, Iterable

from semaphore.reference import FlagsReference

class Flags:

    """An extensible representation of mutable flags."""

    def __init__(
        self, 
        data: Optional[bytearray] = None,
        reference: Optional[FlagsReference] = None
    ) -> None:
        """
        Initialize a new Flags object.
        
        :param data:
            The initial data to set the flags to. Must be a bytearray, because allowing strings or integers 
            can be misinterpreted (e.g., integers as bits or integers representing an existing bitfield). 
            
            You can initialize a new Flags object using one of the ``from_hex``, ``from_array``, ``from_bits``,
            or ``from_flags`` constructors.
            
        :param reference: [optional]
            A reference to use when resolving flag names to bit positions.
        """
        if data is not None and not isinstance(data, bytearray):
            raise TypeError(
                f"`data` must be a bytearray, not {type(data)}. Use the `from_hex`, `from_array`, "
                f"`from_bits`, or `from_flags` constructors"
            )
        self.data = data or bytearray()
        self.reference = reference
        return None
    

    @classmethod
    def from_hex(cls, hex: str, reference: Optional[FlagsReference] = None):
        """
        Initialize a new Flags object from a hexadecimal string.

        :param reference: [optional]
            A reference to use when resolving flag names to bit positions.
        """
        return cls(bytearray.fromhex(hex), reference=reference)


    @classmethod
    def from_array(cls, array: np.array, reference: Optional[FlagsReference] = None):
        """
        Initialize a new Flags object from an integer array.
        
        :param array:
            An array of 8-bit integers to construct the flags from.

        :param reference: [optional]
            A reference to use when resolving flag names to bit positions.
        """
        return cls(bytearray(array), reference=reference)


    @classmethod
    def from_bits(cls, bits: Iterable[int], reference: Optional[FlagsReference] = None):
        """
        Initialize a new Flags object from a list of bits.

        :param bits:
            An iterable of bits to set.
        
        :param reference: [optional]
            A reference to use when resolving flag names to bit positions.
        """
        return cls(reference=reference).set_bits(*bits)


    @classmethod
    def from_flags(cls, flags: Iterable[str], reference: FlagsReference):
        """
        Initialize a new Flags object from a list of flag names.
        
        :param flags:
            An iterable of flag names to set.
        
        :param reference:
            A reference to use when resolving flag names to bit positions.
        """
        return cls(reference=reference).set_flags(*flags)


    @property
    def hex(self):
        """Represent the flags as a hexadecimal string."""
        return self.data.hex()


    @property
    def array(self):
        """Represent the flags as a Numpy array."""
        return np.frombuffer(self.data, dtype=np.uint8)
    
    
    @property
    def bits(self):
        """Represent the flags as a tuple of all bits that are set."""
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


    def set_bits(self, *bits: Iterable[int]) -> None:
        """
        Set the given bit(s).
        
        :param *bits:
            An iterable of bit(s) to set.
        """
        for bit in bits:
            num, offset = self._ensure_length_for_bit(bit)
            self.data[num] |= (1 << offset)
        return self
    
    
    def set_flags(self, *flags: Iterable[str]) -> None:
        """
        Set the given flag(s).
        
        :param *flags:
            An iterable of flag names to set.
        """
        return self.set_bits(*map(self.get_bit_position, flags))


    def clear_bits(self, *bits: Iterable[int]) -> None:
        """
        Clear the given bits.
        
        :param *bits:
            An iterable of bits to clear.
        """
        for bit in set(bits):
            num, offset = self._ensure_length_for_bit(bit)
            self.data[num] &= ~(1 << offset)
        return self
    
    
    def clear_flags(self, *flags: Iterable[str]) -> None:
        """
        Clear the given flag(s).
        
        :param *flags:
            An iterable of flag names to clear.
        """
        return self.clear_bits(*map(self.get_bit_position, flags))


    def toggle_bits(self, *bits: Iterable[int]) -> None:
        """
        Toggle the given bits.
        
        :param *bits:
            An iterable of bits to toggle. If the same bit appears many times in `bits`,
            it will only be toggled once.
        """
        for bit in set(tuple(bits)):
            num, offset = self._ensure_length_for_bit(bit)
            self.data[num] ^= (1 << offset)
        return self
        
    
    def toggle_flags(self, *flags: Iterable[str]) -> None:
        """
        Toggle the given flags.
        
        :param *flags:
            An iterable of flag names to toggle. If the same flag appears many times in `flags`,
            it will only be toggled once.
        """
        return self.toggle_bits(*map(self.get_bit_position, flags))
    

    def is_bit_set(self, bit: int) -> bool:
        """
        Return True if the given bit is set.
        
        :param bit:
            The bit to check.
        """
        # TODO: don't ensure length for bit,.. it expands the bytearray even if we don;t have the bit!
        num, offset = self._ensure_length_for_bit(bit)
        return bool(self.data[num] & (1 << offset))
    
    
    def is_flag_set(self, flag: str) -> bool:
        """
        Return True if the given flag is set.
        
        :param flag:
            The flag to check.
        """
        return self.is_bit_set(self.get_bit_position(flag))
    

    def are_any_bits_set(self, *bits: Iterable[int]) -> bool:
        """
        Return True if any given bits are set.
    
        :param *bits:
            An iterable of bits to check.
        """
        return any(self.is_bit_set(bit) for bit in bits)
    

    def are_any_flags_set(self, *flags: Iterable[str]) -> bool:
        """
        Return True if any given flags are set.
        
        :param *flags:
            An iterable of flags to check.
        """
        return any(self.is_flag_set(flag) for flag in flags)
    

    def are_all_bits_set(self, *bits: Iterable[int]) -> bool:
        """
        Return True if all given bits are set.
        
        :param *bits:
            An iterable of bits to check.
        """
        return all(self.is_bit_set(bit) for bit in bits)


    def are_all_flags_set(self, *flags: Iterable[str]) -> bool:
        """
        Return True if all given flags are set.
        
        :param *flags:
            An iterable of flags to check.
        """
        return all(self.is_flag_set(flag) for flag in flags)


    def __len__(self):
        return len(self.data)


    def _ensure_length_for_bit(self, bit: int) -> Tuple[int, int]:
        num, offset = divmod(bit, 8)
        size = len(self.data)
        if size <= num:
            self.data.extend(b'\x00' * ((num + 1) - size))
        return (num, offset)


    def __repr__(self):
        return f"<{self.__class__.__name__} at {hex(id(self))}>"
    

    def __str__(self):
        return self.hex()