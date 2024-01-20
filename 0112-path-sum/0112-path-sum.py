# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        
        path = []
        
        def get_path(root) :
            if not root :
                return False
            path.append(root.val)

            if not root.left and not root.right :
                path_sum = sum(path)
                if path_sum == targetSum :
                    return True
                else :
                    path.pop()
                    return False
            if get_path(root.left) :
                return True
            if get_path(root.right) :
                return True
            path.pop()
            return False
        
        return get_path(root)
            
        
        