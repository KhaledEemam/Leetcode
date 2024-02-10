class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        i , l , r = len(nums1) -1 , m -1 , n-1
        
        while r >= 0 and l >= 0  :
            if nums1[l] >= nums2[r] :
                nums1[i] = nums1[l]
                l -= 1
                i -= 1
            else :
                nums1[i] = nums2[r]
                r -= 1
                i -= 1
                
        if l == -1 :
            nums1[:i+1] = nums2[:r+1]
                
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
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
            
        """
            
                
                

        
                
                
        