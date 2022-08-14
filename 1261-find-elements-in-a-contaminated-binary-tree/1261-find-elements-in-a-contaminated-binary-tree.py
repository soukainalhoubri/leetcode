# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class FindElements:
    def __init__(self, root: Optional[TreeNode]):
        self.found=set([0])
        q=deque()
        root.val=0
        q.append(root)
        while q:
            current=q.popleft()
            if current.left:
                current.left.val=2*current.val+1
                q.append(current.left)
                self.found.add(current.left.val)
            if current.right:
                current.right.val=2*current.val+2
                q.append(current.right)
                self.found.add(current.right.val)

    def find(self, target: int) -> bool:
        return target in self.found
        


# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)