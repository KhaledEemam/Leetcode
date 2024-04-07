class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        if len(nums) == 0 : 
            return -1
        
        left  , right = 0 , sum(nums)
        for i in range(len(nums)) :
            if (i-1) >= 0 :
                left += nums[i-1]
            right -= nums[i]
            if left == right :
                return i

        return -1
                      
                
            
        
        
        