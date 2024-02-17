from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        queue = deque()
        
        if root:
            queue.append(root)
            
        while queue:
            queue_length = len(queue)
            level_list = []
            for i in range(queue_length):
                cur = queue.popleft()
                
                if cur :
                    level_list.append(cur.val)
                    queue.append(cur.left)
                    queue.append(cur.right)
                else :
                    level_list.append(None)
                    
            
            # Check for symmetry in level_list
            n = len(level_list)
            for i in range(n // 2):
                if level_list[i] != level_list[n - 1 - i]:
                    return False
                    
        return True
        