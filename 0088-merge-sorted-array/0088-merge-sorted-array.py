class Solution(object):
    def merge(self, nums1, m, nums2, n):
        if n == 0:
            first_array = nums1[:]
        else:
            first_array = nums1[:-n]
            
        final = first_array + nums2
        
        for i in range(n) :
            nums1[m+i] = final[m+i]
            
        nums1.sort()
        
        