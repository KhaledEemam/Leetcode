# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        def dfs(node) :
            if not node :
                return None
            
            if node == p :
                return p
            if node == q :
                return q
            
            lnode = dfs(node.left)
            rnode = dfs(node.right)
            
            if not lnode and not rnode :
                return None
            if lnode and not rnode :
                return lnode
            if rnode and not lnode :
                return rnode
            if lnode and rnode :
                return node
            
        return dfs(root)
            
            
                