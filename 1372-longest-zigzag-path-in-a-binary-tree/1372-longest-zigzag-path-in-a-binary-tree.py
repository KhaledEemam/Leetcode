# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:

        longest_length = float("-inf")
        
        def dfs(node,left,right):
            
            nonlocal longest_length
            if not node :
                return
            
            longest_length = max(longest_length,left,right)

                
            if node.left :
                dfs(node.left,1+right,0)
            
            if node.right :
                dfs(node.right , 0 ,left+1)
                
                
        dfs(root,0,0)
        return longest_length