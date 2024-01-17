# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    
    def merged_sort(self,list_1,list_2):
        dummy = ListNode(0)
        tail = dummy
        
        while list_1 and list_2 :
            if list_1.val < list_2.val :
                tail.next = list_1
                list_1 = list_1.next
            else :
                tail.next = list_2
                list_2 = list_2.next
            tail = tail.next
        if list_1 :
            tail.next = list_1
        if list_2 :
            tail.next = list_2
        
        return dummy.next
                
        
    
    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) == 0 or not lists:
            return None
        
        while len(lists) > 1 :
            merged_lists = []
            for i in range(0,len(lists),2) :
                list_1 = lists[i]
                list_2 = lists[i+1] if(i+1)< len(lists) else None
                merged_lists.append(self.merged_sort(list_1,list_2))
            lists = merged_lists
        return lists[0]
        
        #i = len(lists)
        #if i == 1 :
        #   return lists[0]
        
        #list_1 = self.mergeKLists(lists[0:i//2])
        #list_2 = self.mergeKLists(lists[i//2:])
        
        #return self.merged_sort(list_1,list_2)