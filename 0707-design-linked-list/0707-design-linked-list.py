class ListNode :
    def __init__(self,value,next_node=None,prev_node=None) :
        self.val = value
        self.next = next_node
        self.prev = prev_node

class MyLinkedList:

    def __init__(self):
        self.left = ListNode(-11)
        self.right = ListNode(-12)
        
        self.left.next = self.right
        self.right.prev = self.left

    def get(self, index: int) -> int :
        curr = self.left.next
        while curr and index > 0 :
            curr = curr.next
            index -= 1
            
        if curr and curr != self.right and index == 0 :
            return curr.val
        
        return -1
            
            
    def addAtHead(self, val: int) -> None:
        new_head , prev , next = ListNode(val) , self.left , self.left.next
        
        prev.next = new_head
        next.prev = new_head
        new_head.prev = prev
        new_head.next = next
        
        

    def addAtTail(self, val: int) -> None:
        new_tail , prev , next = ListNode(val) , self.right.prev , self.right
        
        prev.next = new_tail
        next.prev = new_tail
        new_tail.prev = prev
        new_tail.next = next
        

    def addAtIndex(self, index: int, val: int) -> None:
        next = self.left.next
        while next and index > 0:
            next = next.next
            index -= 1
        
        if next and index == 0:
            node, prev = ListNode(val), next.prev
            node.next, node.prev = next, prev
            next.prev = node
            prev.next = node
        

    def deleteAtIndex(self, index: int) -> None:
        curr = self.left.next
        
        while curr and index > 0 :
            index -= 1
            curr = curr.next
        
        if curr and curr != self.right and index ==0 :
            prev , next = curr.prev , curr.next
            
            prev.next = next
            next.prev = prev
            


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)