
import heapq 

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        if len(nums) == 1 :
            return nums[0]
        
        nums = [-x for x in nums]
        heapq.heapify(nums)
        
        n = 0
        while k > n and len(nums) > 0 :
            res = heapq.heappop(nums)
            n += 1
            
        return -res
        