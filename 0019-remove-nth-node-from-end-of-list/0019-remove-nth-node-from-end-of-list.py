# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        nodes = []
        cur = head
        while cur :
            nodes.append(cur)
            cur = cur.next
            
        if len(nodes) == 1 :
            return None
        
        index_to_delete = len(nodes) - n
            
        if index_to_delete == 0 :
            return nodes[index_to_delete+1]
        else :
            nodes[index_to_delete-1].next = nodes[index_to_delete].next
            
        return nodes[0]