# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        
        def dfs(root) :
            if not root :
                return root
            if not root.left and not root.right :
                return root
            
            left_nodes  = dfs(root.left)
            right_nodes = dfs(root.right)
            
            if root.left :
                left_nodes.right = root.right
                root.right = root.left
                root.left = None
                
            return right_nodes if right_nodes else left_nodes
        
        dfs(root)
        