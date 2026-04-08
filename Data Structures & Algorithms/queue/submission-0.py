class Node:
    def __init__(self, val):
        self.next = None
        self.val = val
        self.prev = None

class Deque:
    
    def __init__(self):
        self.left = Node(-1)
        self.right = Node(-1)
        self.left.next = self.right
        self.right.prev = self.left


    def isEmpty(self) -> bool:
        if self.left.next == self.right:
            return True
        return False
        

    def append(self, value: int) -> None:
        node = Node(value)
        self.right.prev.next = node
        node.prev  = self.right.prev
        self.right.prev = node
        node.next = self.right


    def appendleft(self, value: int) -> None:
        head = self.left.next
        new = Node(value)
        new.next = head
        head.prev = new
        new.prev = self.left
        self.left.next = new
        

    def pop(self) -> int:
        if self.isEmpty():
            return -1
        val = self.right.prev.val
        t = self.right.prev.prev
        self.right.prev.prev.next = self.right
        self.right.prev = t
        return val
        

    def popleft(self) -> int:
        if self.isEmpty():
            return -1
        val = self.left.next.val
        self.left.next = self.left.next.next
        self.left.next.prev = self.left
        return val
        
        
