# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        
        def dfs(root,leafs) :
            if not root :
                return None
            
            if root.left :
                dfs(root.left,leafs)
            
            if root.right :
                dfs(root.right,leafs)
                
            if not root.left and not root.right :
                leafs.append(root.val)
                
                
        leafs1 , leafs2 = [] , []
        dfs(root1,leafs1)
        dfs(root2,leafs2)
        
        
        if len(leafs1) != len(leafs2) :
            return False
        
        for i in range(len(leafs1)) :
            if leafs1[i] != leafs2[i] :
                return False
            
        return True
        