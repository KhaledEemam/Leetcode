# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        no_of_nodes = float("inf")
        
        if head and head.next :
            for i in range(k) :
                old_head = head
                cur = head
                prev = cur
                no_of_nodes = 1
                
                while cur and cur.next:
                    no_of_nodes += 1
                    prev = cur
                    cur = cur.next

                prev.next = None
                cur.next = old_head
                head = cur
                if i+1 == k%no_of_nodes :
                    return head
                    


        return head