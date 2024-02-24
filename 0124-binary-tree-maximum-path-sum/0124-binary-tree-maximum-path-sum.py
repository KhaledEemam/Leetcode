# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = [root.val]
        
        def dfs(node) :
            if not node  :
                return 0
            
            lval = dfs(node.left)
            rval = dfs(node.right)
            lval_max = max(0,lval)
            rval_max = max(0,rval)
            
            res[0] = max(res[0],node.val+lval_max+rval_max)
            
            return max(lval_max+node.val,rval_max+node.val)
            
            
        dfs(root)
        return res[0]
        
            
            
            
        