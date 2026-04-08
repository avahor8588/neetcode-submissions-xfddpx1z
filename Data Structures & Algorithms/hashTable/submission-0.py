class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None


class HashTable:
    def __init__(self, capacity: int):
        self.cap = capacity
        self.size = 0
        self.table = [None] * self.cap

    def hash(self, key):
        return key % self.cap

    def insert(self, key: int, value: int) -> None:
        i = self.hash(key)
        node = self.table[i]
        if node is None:
            self.table[i] = Node(key, value)
            self.size += 1
        else:
            prev = None
            while node:
                if node.key == key:
                    node.val = value
                    return
                prev = node
                node = node.next
            prev.next = Node(key, value)
            self.size += 1

        if self.size / self.cap >= 0.5:
            self.resize()

    def get(self, key: int) -> int:
        i = self.hash(key)
        node = self.table[i]
        while node:
            if node.key == key:
                return node.val
            node = node.next
        return -1

    def remove(self, key: int) -> bool:
        i = self.hash(key)
        node = self.table[i]
        dummy = Node(-1, -1)
        dummy.next = node

        prev = dummy
        curr = node
        while curr:
            if curr.key == key:
                prev.next = curr.next
                self.size -= 1
                if dummy.next is None:
                    self.table[i] = None
                else:
                    self.table[i] = dummy.next
                return True
            prev = curr
            curr = curr.next
        return False

    def getSize(self) -> int:
        return self.size

    def getCapacity(self) -> int:
        return self.cap

    def resize(self) -> None:
        self.cap *= 2
        new_table = [None] * self.cap
        for node in self.table:
            while node:
                i = self.hash(node.key)
                if new_table[i] is None:
                    new_table[i] = Node(node.key, node.val)
                else:
                    new_node = new_table[i]
                    while new_node.next:
                        new_node = new_node.next
                    new_node.next = Node(node.key, node.val)
                node = node.next
        self.table = new_table
