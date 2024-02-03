from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        res = []
        queue = deque()
        
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
                    
            res.append(sum(level_nodes)/len(level_nodes))
            
            
        return res
                
            
        