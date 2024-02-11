# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = head
        dummy = ListNode(0)
        res = dummy
        
        while cur :
            count = 1
            while cur.next and cur.val == cur.next.val :
                count += 1
                cur = cur.next
                
            if count == 1 :
                res.next = cur
                res = res.next
                
            cur = cur.next
           
        res.next = None
        return dummy.next