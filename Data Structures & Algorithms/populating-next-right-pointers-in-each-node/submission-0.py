"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        
        q = collections.deque()
        if root:
            q.append(root)
        res = []
        while q:
            temp = []
            for i in range(len(q)):
                node = q.popleft()
                if node:
                    temp.append(node)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            start = temp[0]
            for i in range(1, len(temp)):
                start.next = temp[i]
                start = start.next
        return root
        
                
