# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        nodes = []
        cur = head
        
        while cur :
            if cur in nodes :
                return True
            nodes.append(cur)
            cur = cur.next
            
        return False
            
            
        
        