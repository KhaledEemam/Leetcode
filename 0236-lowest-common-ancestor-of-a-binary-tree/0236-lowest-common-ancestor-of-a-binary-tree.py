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
            
            if node.val == p.val or node.val == q.val :
                return node
            
            left_result = dfs(node.left)
            right_result = dfs(node.right)
            
            if left_result and right_result :
                return node
            
            if left_result :
                return left_result
            
            if right_result :
                return right_result
            
            if  not left_result and not right_result :
                return None
            
        return dfs(root)
            
            
                
        