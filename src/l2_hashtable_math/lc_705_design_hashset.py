class MyHashSet:

    def __init__(self):
        self.size = 1000
        self.table = [[] for _ in range(self.size)]

    def _hash(self, key: int) -> int:
        return key % self.size

    def add(self, key: int) -> None:
        index = self._hash(key)
        if key not in self.table[index]:
            self.table[index].append(key)

    def remove(self, key: int) -> None:
        index = self._hash(key)
        if key in self.table[index]:
            self.table[index].remove(key)

    def contains(self, key: int) -> bool:
        index = self._hash(key)
        return key in self.table[index]
