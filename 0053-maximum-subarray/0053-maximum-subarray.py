class Solution(object):
    def maxSubArray(self, nums):
        _max = prev = nums[0]
        for i in nums[1:] :
            prev = max(i , i+prev)
            _max = max(prev,_max)
        return _max

        