# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        cur_max = float("-inf")
        good_count = 0
        
        def dfs(node,path_max) :
            nonlocal good_count
            if not node :
                return
            
            if node.val >= path_max :
                good_count += 1
                
            if node.left :
                dfs(node.left,max(node.val,path_max))
                
            if node.right :
                dfs(node.right,max(node.val,path_max))
        
        
        dfs(root,cur_max)
        return good_count