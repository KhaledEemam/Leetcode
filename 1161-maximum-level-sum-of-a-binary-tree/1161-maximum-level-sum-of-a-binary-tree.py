# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        result = 0
        cur_level = 0
        max_sum = float("-inf")
        
        queue = deque()
        queue.append(root)
        
        while queue :
            cur_level += 1
            level_sum = 0
            for i in range(len(queue)) :
                node = queue.popleft()
                
                level_sum += node.val
                
                if node.left :
                    queue.append(node.left)
                    
                if node.right :
                    queue.append(node.right)
                    
            if level_sum > max_sum :
                result = cur_level
                max_sum = level_sum
                
        return result
                    
                
                
            
        