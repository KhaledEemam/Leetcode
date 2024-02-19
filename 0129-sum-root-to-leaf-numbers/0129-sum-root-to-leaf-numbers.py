# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        res = []
        def dfs(root,value) :
            if not root :                
                return
            if not root.left and not root.right :
                value = value + str(root.val)
                res.append(int(value))
                return 
            
            value = value + str(root.val)
            
            dfs(root.left,value)
            dfs(root.right,value)
        
        dfs(root,'')
        return sum(res)
        
        