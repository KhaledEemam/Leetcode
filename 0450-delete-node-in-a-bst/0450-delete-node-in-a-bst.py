# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        
        def get_min(cur) :
            while cur.left :
                cur = cur.left
            return cur
        
        def delete_node(node,value) :
            if not node :
                return None
            
            if value > node.val :
                node.right = delete_node(node.right,value)
            elif value < node.val :
                node.left = delete_node(node.left,value)
            else :
                if not node.left :
                    return node.right
                elif not node.right :
                    return node.left
                else :
                    min_node = get_min(node.right)
                    node.val = min_node.val
                    node.right = delete_node(node.right,min_node.val)
            
            return node
            
        
        return delete_node(root,key)
                
    
                    
                    
                
                
        