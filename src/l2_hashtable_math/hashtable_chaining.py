from typing import Any, List, Tuple, Optional


class HashMapChaining:
    """
    A simple implementation of a hash map using chaining for collision resolution.
    """

    def __init__(self, size: int = 10) -> None:
        """
        Initializes the hash map with a specified size.

        Args:
            size (int): The initial size of the hash table.
        """
        self.size = size
        self.table: List[List[Tuple[Any, Any]]] = [[] for _ in range(size)]

    def _hash(self, key: Any) -> int:
        """
        Hash function to compute the index for a given key.

        Args:
            key: The key to be hashed.

        Returns:
            int: The hash index.
        """
        return hash(key) % self.size

    def insert(self, key: Any, value: Any) -> None:
        """
        Inserts a key-value pair into the hash map.

        Args:
            key: The key to be inserted.
            value: The value to be associated with the key.
        """
        index = self._hash(key)
        for i, pair in enumerate(self.table[index]):
            if pair[0] == key:
                self.table[index][i] = (key, value)
                return
        self.table[index].append((key, value))

    def delete(self, key: Any) -> None:
        """
        Deletes a key-value pair from the hash map.

        Args:
            key: The key to be deleted.
        """
        index = self._hash(key)
        for i, pair in enumerate(self.table[index]):
            if pair[0] == key:
                del self.table[index][i]
                return

    def search(self, key: Any) -> Optional[Any]:
        """
        Searches for a value associated with a key in the hash map.

        Args:
            key: The key to search for.

        Returns:
            Optional[Any]: The value associated with the key, or None if the key is not found.
        """
        index = self._hash(key)
        for pair in self.table[index]:
            if pair[0] == key:
                return pair[1]
        return None
