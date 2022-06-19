# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        if not root:
            return []
        res, stack = [], [(root, "")]
        while stack:
            node, ls = stack.pop()
            if not node.left and not node.right:
                res.append(ls+str(node.val))
            if node.left:
                stack.append((node.left, ls+str(node.val)+"->"))
            if node.right:
                stack.append((node.right, ls+str(node.val)+"->"))
            
        return res
#         if root is None:
#             return []
#         def paths(node,path,result):
#             if not node.left and not node.right:
#                 result.append(path)
#             elif node.left:
#                 path+="->"+str(node.left.val)
#                 return paths(node.left,path,result)
#             elif node.right:
#                 path+="->"+str(node.right.val)
#                 return paths(node.right,path,result)
#             return result
        
#         return paths(root,str(root.val),[])