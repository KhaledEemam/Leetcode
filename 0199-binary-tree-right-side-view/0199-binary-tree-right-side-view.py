from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        queue = deque()
        res = []
        if root :
            queue.append(root)
            
        while queue :
            queue_length = len(queue)
            for i in range(queue_length) :
                
                cur = queue.popleft()
                
                if i == queue_length-1 :
                    res.append(cur.val)
                
                if cur.left:
                    queue.append(cur.left)
                if cur.right :
                    queue.append(cur.right)
                    
        return res