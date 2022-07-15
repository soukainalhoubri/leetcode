"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
from collections import deque
class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        #we first deal with the edge case:
        if not node:
            return node
        
        q=deque()
        q.append(node)
        values={}#in the dictionnary, we associate to every integer value the newly created node with the same value and an empty list of neighbors, to be populated later
        visited=set()
        while q:
            current=q.popleft()
            if current.val not in values:
                    node=Node(current.val)
                    values[current.val]=node
            if current.val not in visited:
                for n in current.neighbors:
                    if n.val not in values:
                        node=Node(n.val,[])
                        values[n.val]=node
                    values[current.val].neighbors.append(values[n.val])
                    if n.val not in visited:
                        q.append(n)
            visited.add(current.val)
                    
        return values[1]
    