"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        
        adj_list = {}
        def cloning(node) :
            if node in adj_list :
                return adj_list[node]
                    
            new_node = Node(node.val)
            adj_list[node] = new_node
            for i in node.neighbors :
                new_node.neighbors.append(cloning(i))
                
                
            return new_node
        
        return cloning(node) if node else None