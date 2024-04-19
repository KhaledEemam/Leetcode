class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left , right = [0] * len(nums) , [0] * len(nums)
        left[0] = nums[0]
        right[-1] = nums[-1]
        
        for i in range(1,len(nums)) :
            left[i] = left[i-1] * nums[i]
            
        for i in range(len(nums)-2,-1,-1) :
            right[i] = right[i+1] * nums[i]
            
        res = [0] * len(nums)
        res[0] = right[1]
        res[-1] = left[-2]
        
        for i in range(1,len(nums)-1) :
            res[i] = left[i-1] * right[i+1]
            
        return res
            