class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        if len(nums) == 1 :
            return True
        
        increase , decrease = True , True
        
        for i in range(1,len(nums)) :
            if nums[i] > nums[i-1] :
                increase = False
            
            if nums[i] < nums[i-1] :
                decrease = False

        
        return increase | decrease