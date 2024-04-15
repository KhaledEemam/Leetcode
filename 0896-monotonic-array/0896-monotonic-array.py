class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        if len(nums) == 1 :
            return True
        
        def check_monotone_increasing(numbers) :
            for i in range(1,len(nums)) :
                if nums[i] < nums[i-1] :
                    return False
            
            return True
        
        def check_monotone_decreasing(numbers) :
            for i in range(1,len(nums)) :
                if nums[i] > nums[i-1] :
                    return False
            
            return True
        
        monotone = check_monotone_increasing(nums) | check_monotone_decreasing(nums)
        
        return monotone
        
        
