# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pruneTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        def dfs(node) :
            if not node :
                return 0
            
            left_node_val = dfs(node.left)
            right_node_val = dfs(node.right)

            if left_node_val == 0 :
                node.left = None
            
            if right_node_val == 0 :
                node.right = None
            
            return max(left_node_val,right_node_val) + node.val

        
        tree_val = dfs(root)

        if tree_val == 0 :
            return None
        else :
            return root 
        