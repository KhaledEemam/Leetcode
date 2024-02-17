# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        
        
        def dfs(nums_list) :
            if len(nums_list) == 0 :
                return None
            
            l , r = 0 , len(nums_list)-1
            m = (l+r)//2
            
            root = TreeNode(val = nums_list[m])
            
            root.left = dfs(nums_list[:m])
            if m+1 < len(nums_list) :
                root.right = dfs(nums_list[m+1:])
                
            return root
        
        return dfs(nums)
            