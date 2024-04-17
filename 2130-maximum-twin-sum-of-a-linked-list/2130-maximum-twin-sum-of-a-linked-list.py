# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        slow , fast = head , head
        
        while fast.next.next :
            slow = slow.next
            fast = fast.next.next
            
        head2 = slow.next
        slow.next = None
        
        # reversing 2nd list
        cur = head2
        prev = None
        
        while cur :
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
            
        head2 = prev
        
        max_sum = float("-inf")
        
        cur1 = head 
        cur2 = head2

        while cur1 :
            max_sum = max(max_sum,cur1.val+cur2.val)
            cur1 = cur1.next
            cur2 = cur2.next
            
        return max_sum
            
            
            
        