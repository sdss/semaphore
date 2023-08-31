from collections import OrderedDict
from typing import Union, Iterable

class FlagsReference:

    """A reference class for mapping flag names (and their attributes) to individual bits."""

    def __init__(self, definitions: Union[Iterable, OrderedDict]) -> None:
        """
        Initialize a new FlagReference object.
        
        :param definitions:
            An iterable of flag names (where flags have no special attributes), or a dictionary of flag definitions where each 
            key is the flag name, and each value is a dictionary of attributes.
        """
        if not isinstance(definitions, (dict, OrderedDict)):
            # Construct a dictionary from this list.
            self.definitions = OrderedDict(zip(definitions, [dict()]*len(definitions)))
        else:
            self.definitions = definitions
        return None


    @classmethod
    def from_table(cls, table, flag_name_key):
        """
        Construct a new FlagReference object from an astropy Table.
        
        :param table:
            A data table, where each column is an attribute, and each row is a flag definition.
        
        :param flag_name_key:
            The column name in `table` that references the name of the flag.
        """

        if flag_name_key not in table.colnames:
            raise ValueError(f"Column {flag_name_key} not found in table")

        definitions = OrderedDict()
        for row in table:
            definitions[row[flag_name_key]] = dict(row)
        
        return cls(definitions)
        


    def by_attribute(self, key, value, return_bits=True):
        """
        Return a tuple of flags or bits that match a given attribute.
        
        :param key:
            The flag attribute to match.
        
        :param value:
            The value of the attribute to match.
        
        :param return_bits: [optional]
            If `True`, return the bits that match the attribute. If `False`, return the flag names that match the attribute.
        """
        matched = []
        for bit, (flag_name, definition) in enumerate(self.definitions.items(), start=1):
            if key in definition and definition[key] == value:
                data = bit if return_bits else flag_name
                matched.append(data)
        return tuple(matched)


    def __lookup_flag__(self, flag_name):
        # TODO: need to be more explicit and restrictive so we dont allow the user to use integers as flag names
        if isinstance(flag_name, str):            
            try:
                return 1 + list(self.definitions.keys()).index(flag_name)
            except:
                raise KeyError(f"No matching flag by name '{flag_name}'")
        elif isinstance(flag_name, int):
            return list(self.definitions.keys())[flag_name - 1]
        else:
            raise ValueError("Flag name must be a string or integer")

    def __getitem__(self, flag_name):
        if isinstance(flag_name, (list, tuple)):
            return tuple(map(self.__lookup_flag__, flag_name))
        else:
            return self.__lookup_flag__(flag_name)