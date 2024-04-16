class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        nums1 , nums2 = sorted(list(set(nums1))) , sorted(list(set(nums2)))
        l , r = 0 , 0
        answer1 , answer2 = [] , []
        
        while l < len(nums1) and r < len(nums2) :
            if nums1[l] == nums2[r] :
                l += 1
                r += 1
            elif nums1[l] < nums2[r] :
                answer1.append(nums1[l])
                l += 1
            else :                 
                answer2.append(nums2[r])
                r += 1
                
        if l == len(nums1) :
            answer2 += nums2[r:]
            
            
        if r == len(nums2) :
            answer1 += nums1[l:]
            
        return [answer1,answer2]
            
            
        