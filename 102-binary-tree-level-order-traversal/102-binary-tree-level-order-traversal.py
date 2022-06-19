# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        " a function to calculate the height of a tree"
        ans, level = [], [root]
        while root and level:
            ans.append([node.val for node in level])
            LRpair = [(node.left, node.right) for node in level]
            level = [leaf for LR in LRpair for leaf in LR if leaf]
        return ans
#         def current_level(root,level):
#             if not root:
#                 return []
#             ans=[]
#             if level==1:
#                 ans.append(root.val)
#             elif level>1:
#                 return current_level(root.left,level-1)
#                 return current_level(root.right,level-1)
#             return ans
            
#         def height(node):
#             if node is None:
#                 return 0
#             left_height=1+height(node.left)
#             right_height=1+height(node.right)
            
#             # if left_height>right_height:
#             #     return left_height+1
#             # if left_height<right_height:
#             #     return right_height+1
#             return max(left_height,right_height)
#         if not root:
#             return []
#         ans=[]
#         h=height(root)
#         for i in range(1,h+1):
#             ans.append(current_level(root,i))

            
            
        
        
        
        return ans
        
        
            