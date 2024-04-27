class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums = [-num for num in nums]
        heapq.heapify(nums)
        
        res = None
        for i in range(k) :
            res = -1 * heapq.heappop(nums)
            
        return res