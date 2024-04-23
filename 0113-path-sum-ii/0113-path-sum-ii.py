# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        paths = []
        path_sum = 0
        
        def dfs(node,path_list,path_sum) :
            if not node :
                return
            
            if not node.left and not node.right :
                if (path_sum+node.val) == targetSum :
                    paths.append(path_list + [node.val])
                    
                return
            
            if node.left :
                dfs(node.left,path_list+[node.val],path_sum+node.val)
                
            if node.right :
                dfs(node.right,path_list+[node.val],path_sum+node.val)
                
            return
        
        dfs(root,[],0)
        return paths

                
        