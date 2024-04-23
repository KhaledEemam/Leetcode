# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        if not root :
            return 0
        
        def dfs(node,target):
            if not node :
                return 0
            
            count = 0
            if node.val == target :
                count = 1
                
            new_sum = target - node.val
            
            count += dfs(node.left,new_sum)
            count += dfs(node.right,new_sum)
            return count
            
            
            
        return self.pathSum(root.left,targetSum) + self.pathSum(root.right,targetSum) + dfs(root,targetSum)
            