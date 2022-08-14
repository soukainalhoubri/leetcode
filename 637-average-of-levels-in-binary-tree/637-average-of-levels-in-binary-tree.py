# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        q=deque()
        q.append(root)
        answer=list()
        while q:
            _sum=0
            level_length=len(q)
            for i in range(level_length):
                node=q.popleft()
                _sum+=node.val
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            answer.append(round(_sum/level_length,5))
                
        return answer
            