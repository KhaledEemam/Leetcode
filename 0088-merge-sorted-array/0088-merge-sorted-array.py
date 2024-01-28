class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        nums1_divided = nums1[:m]
        
        i , k , h = 0 , 0 , 0 
        
        while i < m and k < n :
            if nums1_divided[i] < nums2[k] :
                nums1[h] = nums1_divided[i]
                i += 1
                h += 1
            elif nums1_divided[i] > nums2[k] :
                nums1[h] = nums2[k]
                k += 1
                h += 1
            else :
                nums1[h] , nums1[h+1] = nums1_divided[i] , nums2[k] 
                h += 2
                k+= 1
                i += 1
                
                
                
        if i == m :
            nums1[h:] = nums2[k:]
        elif k == n :
            nums1[h:] = nums1_divided[i:]
            
                
                

        
                
                
        