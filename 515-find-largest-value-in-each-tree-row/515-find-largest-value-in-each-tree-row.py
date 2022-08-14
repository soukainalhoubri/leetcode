# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        
        if not root:
            return result
        q = deque()
        
        q.append(root)

        
        while q:
            level_len = len(q)
            maximum = float('-inf')
            for _ in range(level_len):
                node = q.popleft()
                maximum = max(maximum, node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            result.append(maximum)
        return result