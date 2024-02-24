# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        def get_kth(cur,k) :
            while cur and k > 0 :
                cur = cur.next
                k -= 1
            return cur

    
        dummy = ListNode()
        dummy.next = head
        groupprev = dummy
        
        while True :
            kth = get_kth(groupprev,k)
            if not kth :
                break
                
            groupnext = kth.next
            
            prev , cur = kth.next , groupprev.next
            
            while cur != groupnext :
                temp = cur.next
                cur.next = prev
                prev = cur
                cur = temp
                
            temp = groupprev.next
            groupprev.next = kth
            groupprev = temp
        
        return dummy.next