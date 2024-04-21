class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        count = 1
        nums.sort()
        
        for i in range(1,len(nums)) :
            if nums[i] != nums[i-1] and count == 1 :
                return nums[i-1]
            elif nums[i] == nums[i-1] :
                count += 1
            elif nums[i] != nums[i-1] :
                count = 1
        return nums[-1]