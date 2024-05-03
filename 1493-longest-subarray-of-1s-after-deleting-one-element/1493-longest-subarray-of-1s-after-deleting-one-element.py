class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        left = [0] * len(nums)
        right = [0] * len(nums)
        
        consec_ones = 0
        
        for i in range(len(nums)) :
            left[i] = consec_ones
            
            if nums[i] == 1 :
                consec_ones += 1
            else :
                consec_ones = 0
         
        consec_ones = 0
        for i in range(len(nums)-1,-1,-1):
            right[i] = consec_ones
            
            if nums[i] == 1 :
                consec_ones += 1
            else :
                consec_ones = 0
                
        max_res = float("-inf")
        for i in range(len(nums)) :
            cur_sum = left[i] + right[i]
            max_res = max(max_res,cur_sum)
            
        return max_res
            
        
                
            
            
        