from typing import TypeVar, List, Tuple, Generic, Any, Union, Optional
from functools import reduce

T = TypeVar("T")

class hash_table(Generic[T]):
    @staticmethod
    def hasher_homemade_2(key: str, array_len: int) -> int:
        """Returns an integer representation of the key that is below a given array length

        notes:
            - uses the standard library default `hash` function
        """
        return abs(hash(key)) % array_len

    @staticmethod
    def hasher_homemade_1(key: str, array_len: int) -> int:
        """
        requirements:
        - constant time O(1)
        - even distribution of integer values
        - changes rapidly for small perturbations in input (chaotic)
        - can take any primitive or structural object

        limitations:
        - key hashing only considers the first 100 characters
        """
        total = 0
        WEIRD_PRIME = 31
        for i in range(min([len(key), 100])):
            char = key[i]
            value = ord(char) - 96
            total = (total * WEIRD_PRIME + value) % array_len
        return total

    @staticmethod
    def _find_item(
        array: List[Tuple[str, T]], target_key: T
    ) -> Union[Tuple[str, T], None]:
        """Returns the tuple that matches the key exactly in the tuple array

        args:
            array: list of key, item tuples
            target_key: key to match with the tuple

        time: O(n)
        """
        found_items = [tp for tp in array if tp[0] == target_key]
        if len(found_items) == 0:
            return None
        return found_items[0]

    def __init__(self, array_len: int = 31, hash_fn=hasher_homemade_2) -> None:
        # TODO: shouldn't this be a List of List of tuples?
        # TODO: what if identical keys? to prevent that it should be a list of Set of tuples
        self.keymap: List[Optional[List[Tuple[str, T]]]] = [None] * array_len
        self.hasher = lambda item: hash_fn(item, array_len)
        self.array_len = array_len

    def set(self, key: int, item: T) -> None:
        """uses separate chaining method"""
        hashed_key = self.hasher(key)
        if self.keymap[hashed_key] == None:
            self.keymap[hashed_key] = []
        self.keymap[hashed_key].append((key, item))

    def get(self, key) -> Union[Tuple[str, T], None]:
        """Returns a key, value tuple for a given key from the hashtable"""
        # check if key has items
        hashed_key = self.hasher(key)
        if self.keymap[hashed_key] == None:
            return None

        # retrieve the array for key
        key_array = self.keymap[hashed_key]

        # find the tuple with the target key
        item_pair = hash_table._find_item(key_array, key)
        return item_pair
    
    def keys(self) -> List[str]:
        """Returns a list of keys present in the hash table"""
        key_list: List[str] = []
        for hash_bucket in self.keymap:
            if hash_bucket is None:
                continue
            
            # approach 1
            # causes entire array to be instantiated in each iteration
            # # cannot use append because <Array>.append -> None
            # # which causes NoneType errors in the next iteration
            # O(n!)
            collect = lambda collected, item: [*collected, item[0]]
            key_list = reduce(collect, hash_bucket, key_list)

            # approach 2
            # for item in hash_bucket:
            #     key_list.append(item[0])

        return key_list

    def values(self) -> List[str]:
        """Returns a list of values present in the hash table, includes duplicate instances"""
        value_list: List[str] = []
        for hash_bucket in self.keymap:
            if hash_bucket is None:
                continue
            
            for item in hash_bucket:
                value_list.append(item[1])

        return value_list

    def __repr__(self) -> str:
        return repr(f"hashtable: length({self.array_len})")
