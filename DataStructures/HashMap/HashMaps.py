
from typing import List, Any, Tuple


class HashMap:
    """
    Implements a hash map (associative container) with a fixed number
    of buckets. It supports string keys and values of any type.
    """
    size : int
    table : List[List[Tuple[str, Any]]]

    def __init__(self, size: int):
        """
        Creates an empty HashMap with <size> buckets.

        >>> hash_map0 = HashMap(0)
        >>> hash_map1 = HashMap(5)
        """
        self.size = size
        self.table = [
            [] for _ in range(size)
        ]

    def insert(self, key: str, value: Any) -> None:
        """
        Insert or updates the value to <value> for a given key <key>.

        >>> hash_map = HashMap(5)
        >>> hash_map.insert("test", 5)
        >>> hash_map.lookup("test")
        5
        >>> hash_map.insert("test", "wert")
        >>> hash_map.lookup("test")
        'wert'
        """
        h = self.key_hash(key) % self.size
        bucket = self.table[h]
        for i, (k, _) in enumerate(bucket):
            if k == key:
                bucket[i] = (key, value)
                return
        bucket.append((key, value))

    def lookup(self, key: str) -> Any:
        """
        Return the stored value or None if there is no value
        stored for the key.

        >>> hash_map = HashMap(5)
        >>> not hash_map.lookup("test")
        True
        >>> hash_map.lookup("test") is None  # lookup will not insert!
        True
        >>> hash_map.insert("test", "wert")
        >>> hash_map.lookup("test")
        'wert'
        """
        h = self.key_hash(key) % self.size
        bucket = self.table[h]
        for (k, value) in bucket:
            if k == key:
                return value

    def key_value_pairs(self) -> List[Tuple[str, Any]]:
        """
        Get a list of all (key, value) pairs stored in the
        hash map. This can be used to iterate over the entire map.

        >>> hash_map = HashMap(50)
        >>> hash_map.key_value_pairs()
        []

        >>> hash_map.insert("truth", 42)
        >>> hash_map.insert("NotJustNumbers", "value")
        >>> key_values = hash_map.key_value_pairs()
        >>> # sort so the order is independent of the hash function
        >>> sorted(key_values, key = lambda pair: pair[0])
        [('NotJustNumbers', 'value'), ('truth', 42)]
        """
        result = []
        for buckets in self.table:
            for (key, value) in buckets:
                result.append((key, value))
        return result

    def max_entries_same_hash(self) -> int:
        """
        Return the maximum number of elements hashed to the same value.

        >>> hash_map = HashMap(1)
        >>> hash_map.insert("truth", 42)
        >>> hash_map.insert("NotJustNumbers", "value")
        >>> hash_map.max_entries_same_hash()
        2
        """
        max_entries_in_hash = 0
        for bucket in self.table:
            if len(bucket) > max_entries_in_hash:
                max_entries_in_hash = len(bucket)
        return max_entries_in_hash

    @staticmethod
    def key_hash(key: str) -> int:
        """
        Hashes a given string returning an int value.

        >>> type(HashMap.key_hash('ceiling')) == int
        True
        >>> type(HashMap.key_hash('floor')) == int
        True
        >>> HashMap.key_hash('poison') != HashMap.key_hash('food')
        True
        """
        sum = 0
        B = 257
        for char in key:
            sum = sum * B + ord(char)
        return sum