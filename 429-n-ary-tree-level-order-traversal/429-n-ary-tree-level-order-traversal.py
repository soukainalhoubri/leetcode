"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
from collections import deque
class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root:
            return []
        q=deque()
        q.append(root)
        result=[]
        while q:
            level_length=len(q)
            current_level=[]
            for _ in range(level_length):
                current=q.popleft()
                current_level.append(current.val)
                #populate the q
                for child in current.children:
                    q.append(child)
            result.append(current_level)
        return result
            