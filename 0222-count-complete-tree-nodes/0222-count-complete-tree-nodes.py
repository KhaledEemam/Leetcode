# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        
        def dfs(root) :
            if not root :
                return 0
            
            cur = root
            lh , rh = 0 , 0
            
            while cur.left :
                cur = cur.left
                lh += 1
                
            while cur.right :
                cur = cur.right
                rh  += 1
                
            if lh == rh :
                return 1+rh+lh
            
            lh = dfs(root.left)
            rh = dfs(root.right)
            
            return lh + rh + 1
        
        return dfs(root)
            
            
            
        
            
        
        