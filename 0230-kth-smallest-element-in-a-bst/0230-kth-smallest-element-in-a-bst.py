# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        res = []
        
        def inorder(root) :
            if not root :
                return None

            inorder(root.left)
            res.append(root.val)
            inorder(root.right)
            
        """    
        def sort_merge_lists(list_1,list_2) :
            total_length = len(list_1) + len(list_2)
            i , n , k = 0 , 0 , 0
            sorted_list = []
            
            while i < total_length :
                if n == len(list_1) :
                    sorted_list += list_2[k:]
                    break
                elif k == len(list_2) :
                    sorted_list += list_1[n:]
                    break
                    
                    
                if list_1[n] > list_2[k] :
                    sorted_list.append(list_2[k])
                    k = k + 1
                    i = i + 1
                elif list_1[n] < list_2[k] :
                    sorted_list.append(list_1[n])
                    n = n + 1 
                    i = i + 1
                else :
                    sorted_list.append(list_1[n])
                    sorted_list.append(list_1[k])
                    i += 2
                    k += 1
                    n += 1
            return sorted_list        
            
            
        def sort(my_list) :
            l , r = 0 , len(my_list) -1
            m = (l+r) // 2
            
            if len(my_list) == 1:
                return my_list
            
            list_1 = sort(my_list[l:m])
            list_2 = sort(my_list[m+1:r+1])
            return sort_merge_lists(list_1,list_1)
            
            """
            
        
        inorder(root)
        return res[k-1]
        
        
            