class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        a , b = nums1 , nums2 
        
        if len(a) > len(b) :
            a , b = b , a
            
        total = len(nums1) + len(nums2)
        half = total // 2
        l , r = 0 , len(a) - 1
        
        while True :
            i = (l+r) // 2
            j = half - i -2 
            
            aleft = a[i] if i >= 0 else float("-infinity")
            aright = a[i+1] if (i+1) < len(a) else float("infinity")
            bleft = b[j] if j >= 0 else float("-infinity")
            bright = b[j+1] if (j+1) < len(b) else float("infinity")
            
            if aleft <= bright and aright >= bleft :
                
                if total % 2 == 1 :
                    return min(aright,bright)
                else :
                    median = (max(aleft,bleft) + min(aright,bright)) / 2
                    return (median)
            else :
                if aleft > bright :
                    r = i -1 
                elif aright < bleft :
                    l = i + 1
        
        