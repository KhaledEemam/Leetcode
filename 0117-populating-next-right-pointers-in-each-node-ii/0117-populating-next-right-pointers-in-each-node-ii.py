"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
import collections
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        
        
        queue = collections.deque()
        
        if root :
            queue.append(root)
            
        while queue :
            prev = None
            queue_length = len(queue)
            for i in range(queue_length) :
                cur = queue.popleft()
                
                if cur.left :
                    queue.append(cur.left)
                    
                if cur.right :
                    queue.append(cur.right)
                 
                if queue_length == 1 :
                    cur.next = None
                elif i == (queue_length-1) :
                    cur.next = None
                    prev.next = cur
                elif i > 0 :
                    prev.next = cur
                    
                    
                prev = cur
                
        
        return root        
                
                
        