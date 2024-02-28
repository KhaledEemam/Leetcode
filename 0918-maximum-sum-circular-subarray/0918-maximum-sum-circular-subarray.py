class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        max_sum = nums[0]
        cur_min_sum = 0
        min_sum = nums[0]
        cur_max_sum = 0
        
        for num in nums :
            
            cur_max_sum = max(num , num+cur_max_sum)
            cur_min_sum = min(num , num+cur_min_sum)
            max_sum = max(max_sum,cur_max_sum)
            min_sum = min(min_sum,cur_min_sum)
            
            
        
        if max_sum < 0 :
            return max_sum
        else :
            return max(max_sum,sum(nums)-min_sum)
            
                
        
                
                