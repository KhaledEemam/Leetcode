from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        queue = deque()
        res = []
        direction = True
        
        if root :
            queue.append(root)
            
        while queue :
            level_nodes = []

            for i in range(len(queue)) :
                cur = queue.popleft()
                level_nodes.append(cur.val)
                if cur.left :
                    queue.append(cur.left)
                if cur.right :
                    queue.append(cur.right)
                        
            if not direction :
                level_nodes.reverse()
                
            res.append(level_nodes)
            direction = not direction
            
        
        return res
                    
            
            