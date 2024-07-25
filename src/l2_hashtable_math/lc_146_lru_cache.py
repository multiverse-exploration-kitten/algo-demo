class SinglyLinkedListNode:
    def __init__(self, key=None, val=None):
        self.key = key
        self.val = val
        self.next = None


class LRUCacheWithSingleLinkedList:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.mapping = {}
        self.head = SinglyLinkedListNode()
        self.tail = self.head

    def push_back(self, node):
        self.mapping[node.key] = self.tail
        self.tail.next = node
        self.tail = node

    def pop_front(self):
        del self.mapping[self.head.next.key]
        self.head.next = self.head.next.next
        self.mapping[self.head.next.key] = self.head

    def kick(self, prev):
        node = prev.next
        if node == self.tail:
            return

        prev.next = node.next
        if node.next:
            self.mapping[node.next.key] = prev
            node.next = None

        self.push_back(node)

    def get(self, key: int) -> int:
        if key not in self.mapping:
            return -1

        self.kick(self.mapping[key])
        return self.mapping[key].next.val

    def put(self, key: int, value: int) -> None:
        if key in self.mapping:
            self.mapping[key].next.val = value
            self.kick(self.mapping[key])
        else:
            new_node = SinglyLinkedListNode(key, value)
            self.push_back(new_node)
            if len(self.mapping) > self.capacity:
                self.pop_front()


class DoublyLinkedListNode:
    def __init__(self, key=None, val=None):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None

    def __str__(self):
        return f"{self.prev.val} <- <DoublyLinkedListNode key: {self.key}, val: {self.val}> -> {self.next.val}"

    def __repr__(self):
        return self.__str__()


class LRUCacheWithDoubleLinkedList:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.mapping = {}
        self.head = DoublyLinkedListNode(val="head")
        self.tail = DoublyLinkedListNode(val="tail")
        self.head.next = self.tail
        self.tail.prev = self.head

    def push_back(self, node):
        self.mapping[node.key] = node
        prev_node = self.tail.prev
        prev_node.next = node
        node.prev = prev_node
        node.next = self.tail
        self.tail.prev = node

    def pop_front(self):
        del self.mapping[self.head.next.key]
        self.head.next = self.head.next.next
        self.head.next.prev = self.head

    def kick(self, node):
        if node == self.tail.prev:
            return

        prev_node = node.prev
        prev_node.next = node.next
        if node.next:
            node.next.prev = prev_node

        self.push_back(node)

    def get(self, key: int) -> int:
        if key not in self.mapping:
            return -1

        self.kick(self.mapping[key])
        return self.mapping[key].val

    def put(self, key: int, value: int) -> None:
        if key in self.mapping:
            self.mapping[key].val = value
            self.kick(self.mapping[key])
        else:
            new_node = DoublyLinkedListNode(key, value)
            self.push_back(new_node)
            if len(self.mapping) > self.capacity:
                self.pop_front()
