# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import collections

class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        if not root : return None
        
        queue = collections.deque()
        queue.append(root)
        row = [root]
        result = None
        
        while queue :
            result  = row[0].val
            row = []
            
            for i in range(len(queue)) :
                node = queue.popleft()
                
                if node.left  :
                    queue.append(node.left)
                    row.append(node.left)
                    
                if node.right :
                    queue.append(node.right)
                    row.append(node.right)
                    
        return result
                    
                
        