"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
from collections import deque
class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':

        if not root :
            return None

        queue = deque()
        queue.append(root)

        while queue :

            mostRightNode = None
            # loop per level
            for _ in range(len(queue)) :
                currentNode = queue.popleft()
                currentNode.next = mostRightNode
                mostRightNode = currentNode

                if currentNode.right :
                    queue.append(currentNode.right)
                
                if currentNode.left :
                    queue.append(currentNode.left)


        return root
        