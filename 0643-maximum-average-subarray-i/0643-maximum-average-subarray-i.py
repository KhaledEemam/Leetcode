class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        result = sum(nums[:k])
        cur_result = sum(nums[:k])
        
        for i in range(k,len(nums)) :
            cur_result = cur_result - nums[i-k] + nums[i]
            result = max(result,cur_result)
            
        return result / k
        