# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        i = 1
        odd_dummy  , even_dummy = ListNode() , ListNode()
        cur_odd , cur_even = odd_dummy , even_dummy
        cur = head
        
        while cur :
            next_node = cur.next
            if i % 2 == 0 :
                # even
                cur_even.next = cur
                cur_even = cur_even.next
            else :
                # odd
                cur_odd.next = cur
                cur_odd = cur_odd.next
                
            i += 1
            cur.next = None
            cur = next_node
            
        cur_odd.next = even_dummy.next
        return odd_dummy.next
        
            
        
        