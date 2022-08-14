# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        q=deque()
        q.append(root)
        depth=0
        while q:
            depth+=1
            level_length=len(q)
            for i in range(level_length):
                current=q.popleft()
                if not current.left and not current.right:
                    return depth
                if current.left:
                    q.append(current.left)
                if current.right:
                    q.append(current.right)
        return depth
        