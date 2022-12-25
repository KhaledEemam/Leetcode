class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(nums)) :
            for y in range(i+1,len(nums)) :
                if nums[i] + nums[y] == target :
                    return [i,y]
        