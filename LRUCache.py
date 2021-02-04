class DLL:
    def __init__(self, key=0, value=0):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class LRUCache:

    def __init__(self, capacity: int):
        self.head = DLL()
        self.tail = DLL()
        self.cache = {}
        self.n = capacity
        self.size = 0

        self.head.next = self.tail
        self.tail.prev = self.head

    def add_node(self, node):
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node
        return node

    def remove_node(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def pop_node(self):
        res = self.tail.prev
        self.remove_node(res)
        return res

    def reorder(self, node):
        self.remove_node(node)
        self.add_node(node)

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1

        node = self.cache.get(key)
        self.reorder(node)
        return node.value

    def put(self, key: int, value: int) -> None:
        if key not in self.cache:
            if self.size < self.n:
                self.size += 1

            else:
                self.cache.pop(self.pop_node().key)

            self.cache[key] = self.add_node(DLL(key, value))

        else:
            node = self.cache.get(key)
            node.value = value
            self.reorder(node)

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)