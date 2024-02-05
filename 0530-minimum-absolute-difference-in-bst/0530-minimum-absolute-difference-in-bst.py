# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        
        res = []
        
        def get_nodes_val(root) :
            
            if not root :
                return None
            
            if not root.left and not root.right :
                res.append(root.val)
                return
            
            cur = root
            if cur.left :
                get_nodes_val(cur.left)
                
            res.append(root.val)
                
            if cur.right :
                get_nodes_val(cur.right)
                

                
        get_nodes_val(root)
        differences = []
        
        for i in range(len(res)-1):
            differences.append(abs(res[i]-res[i+1]))
        
        return min(differences)
            
                
                
            
            
            
            
        
            
            
        
        