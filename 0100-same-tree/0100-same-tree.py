# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        def traverse_tree(root,my_list) :
            if not root :
                my_list.append(None)
                return None
            my_list.append(root.val)
            traverse_tree(root.left,my_list)
            traverse_tree(root.right,my_list)
            
            
        first_tree , second_tree = [] , []
        traverse_tree(p,first_tree)
        traverse_tree(q,second_tree)
        if len(first_tree) != len(second_tree) :
            return False
        
        for i in range(len(first_tree)) :
            if first_tree[i] != second_tree[i] :
                return False
            
        return True
        
            
        