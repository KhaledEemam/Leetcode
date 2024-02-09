# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        remainder = 0
        cur1 , cur1_value = l1 , l1.val
        cur2 , cur2_value = l2 , l2.val
        l3 = ListNode()
        cur_3 = l3
        l1_done , l2_done = False , False
        
        while ((not l1_done) or (not l2_done) or (remainder > 0)):
            cur_sum = cur1_value + cur2_value + remainder
            remainder = 0
            if cur_sum > 9 :
                remainder =  cur_sum // 10
                cur_sum = cur_sum % 10
            
            if cur1 and cur1.next :
                cur1 = cur1.next
                cur1_value = cur1.val
            else :
                cur1_value = 0
                l1_done = True
            
            if cur2 and cur2.next:
                cur2 = cur2.next
                cur2_value = cur2.val
            else :
                cur2_value = 0
                l2_done = True
                
            
            
            cur_3.val = cur_sum
            if l1_done and l2_done and remainder == 0  :
                return l3
            
            
            if not l1_done or not l2_done or remainder > 0:
                cur_3.next = ListNode()
                cur_3 = cur_3.next
            
                
        return l3
            
        