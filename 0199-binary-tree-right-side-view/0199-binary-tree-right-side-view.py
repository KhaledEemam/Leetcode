# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root :
            return []
        
        values = []
        queue = deque()
        queue.append(root)
        
        while queue :
            queue_length = len(queue)
            for i in range(queue_length) :
                node = queue.popleft()
                
                if node.left :
                    queue.append(node.left)
                    
                if node.right :
                    queue.append(node.right)
                
                if i == (queue_length -1) :
                    values.append(node.val)
                    
        return values
                
        