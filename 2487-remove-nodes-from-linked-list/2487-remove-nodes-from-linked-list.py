# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:

        def revrse_LinkedList(listHead) :
            prev = None
            curr = listHead

            while curr :
                temp = curr.next
                curr.next =  prev
                prev = curr
                curr = temp

            return prev

        head = revrse_LinkedList(head)
        curr = head
        maxValue = curr.val

        while curr and curr.next :
            if curr.next.val < maxValue :
                curr.next = curr.next.next
            else :
                maxValue = curr.next.val
                curr = curr.next

        head = revrse_LinkedList(head)
        return head