"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        my_hash = {}
        head_2 = Node(0)
        dummy = head_2
        cur = head
        while cur :
            dummy.next = Node(x = cur.val)
            my_hash[cur] = dummy.next
            dummy = dummy.next
            cur = cur.next
            
            
        for original , copy in my_hash.items() :
            if original.random == None :
                copy.random = None
            else :
                copy.random =  my_hash[original.random]
                
        return head_2.next
            
            
        
        
        