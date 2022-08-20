# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        q=deque()
        q.append(root)
        reverse=0
        answer=[]
        while q:
            level_length=len(q)
            current_level=deque()
            for _ in range(level_length):
                current=q.popleft()
                if current.left:
                    q.append(current.left)
                if current.right:
                    q.append(current.right)
                if reverse%2==0:
                    current_level.append(current.val)
                else:
                    current_level.appendleft(current.val)
            answer.append(current_level)
            reverse+=1
        return answer
            