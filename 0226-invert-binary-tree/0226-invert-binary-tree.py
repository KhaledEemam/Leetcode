# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        def dfs(root) :
            if not root or (not root.left and  not root.right):
                return root
            
            temp = root.left
            root.left = root.right
            root.right = temp
            
            if root.left :
                dfs(root.left)
            
            if root.right :
                dfs(root.right)
                
            return root
        
        return dfs(root)
                
            
            
        