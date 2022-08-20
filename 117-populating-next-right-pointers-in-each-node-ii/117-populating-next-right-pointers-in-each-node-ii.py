"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
from collections import deque
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if root:
            q=deque()
            q.append(root)
            while q:
                level_length=len(q)
                current_level=[]
                for _ in range(level_length):
                    current=q.popleft()
                    current_level.append(current)
                    if current.left:
                        q.append(current.left)
                    if current.right:
                        q.append(current.right)

                for i in range(level_length-1):
                    current_level[i].next=current_level[i+1]
        return root
                