# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        
        def validate(root,min_boundary,max_boundary) :
            
            if not root :
                return None

            if root.val <=  min_boundary or root.val >=  max_boundary :
                return False

            
            if validate(root.left,min_boundary,root.val) == False :
                return False
            if validate(root.right,root.val,max_boundary) == False :
                return False
            
            return True

        
        return validate(root,float("-inf"),float("inf"))
    
    
    

        
        