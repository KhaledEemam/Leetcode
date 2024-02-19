# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next :
            return head
        
        left = head
        right = self.get_mid(head)
        temp = right.next
        right.next = None
        right = temp
        
        left_list = self.sortList(left)
        right_list = self.sortList(right)
        return self.merge_lists(left_list,right_list)
    
    def get_mid(self,node) :
        slow , fast = node , node.next
        while fast and fast.next :
            slow = slow.next
            fast = fast.next.next
            
        return slow
    
    def merge_lists(self,left,right) :
        dummy = tail = ListNode()
        while left and right :
            if left.val <= right.val :
                tail.next = left
                left = left.next
            else :
                tail.next = right
                right = right.next
            tail = tail.next
            
        if left :
            tail.next = left
        if right :
            tail.next = right
        
        return dummy.next
                
        
        