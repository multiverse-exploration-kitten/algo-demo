class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class DoublyLinkedList:
    def __init__(self):
        self.head = Node(None, None)  # Sentinel head
        self.tail = Node(None, None)  # Sentinel tail
        self.head.next = self.tail
        self.tail.prev = self.head

    def add(self, node):
        # Add new nodes right after head
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node

    def remove(self, node):
        # Remove an existing node
        prev, nxt = node.prev, node.next
        prev.next, nxt.prev = nxt, prev

    def pop(self):
        # Pop the least recently used node (right before tail)
        if self.head.next == self.tail:
            return None
        node = self.tail.prev
        self.remove(node)
        return node


class LFUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.node_map = {}  # Key to node
        self.freq_map = {}  # Freq to doubly linked list of nodes
        self.key_freq = {}  # Key to freq
        self.min_freq = 0

    def update_freq(self, key):
        # Helper function to update a key's frequency
        freq = self.key_freq.get(key, 0)
        self.key_freq[key] = freq + 1
        if freq in self.freq_map:
            self.freq_map[freq].remove(self.node_map[key])
            if not self.freq_map[freq].head.next != self.freq_map[freq].tail:
                if freq == self.min_freq:
                    self.min_freq += 1
                del self.freq_map[freq]
        if freq + 1 not in self.freq_map:
            self.freq_map[freq + 1] = DoublyLinkedList()
        self.freq_map[freq + 1].add(self.node_map[key])

    def get(self, key: int) -> int:
        if key not in self.node_map:
            return -1
        self.update_freq(key)
        return self.node_map[key].value

    def put(self, key: int, value: int) -> None:
        if self.capacity == 0:
            return
        if key in self.node_map:
            self.node_map[key].value = value
            self.update_freq(key)
            return
        if len(self.node_map) == self.capacity:
            # Evict least frequently used node
            lfu_list = self.freq_map[self.min_freq]
            node = lfu_list.pop()
            del self.node_map[node.key]
            del self.key_freq[node.key]
        new_node = Node(key, value)
        self.node_map[key] = new_node
        self.min_freq = 1  # Reset min_freq for new node
        self.update_freq(key)
