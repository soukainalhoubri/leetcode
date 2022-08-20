# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        q=deque()
        q.append(root)
        leaves_sum=0
        left_nodes=set()
        while q:
            level_length=len(q)
            current_level=[]
            for _ in range(level_length):
                current=q.popleft()
                current_level.append(current)
                if current.left:
                    q.append(current.left)
                    left_nodes.add(current.left)
                if current.right:
                    q.append(current.right)
            for node in current_level:
                if node in left_nodes and not node.left and not node.right:
                    leaves_sum+=node.val
        return leaves_sum
                