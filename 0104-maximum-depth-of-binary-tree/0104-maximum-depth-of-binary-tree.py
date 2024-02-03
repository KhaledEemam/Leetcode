from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        queue = deque()
        count = 0 
        
        if root :
            queue.append(root)
            
        while queue :
            count += 1
            for i in range(len(queue)) :
                cur = queue.popleft()
                if cur.left :
                    queue.append(cur.left)
                if cur.right :
                    queue.append(cur.right)
                    
        return count
        
        