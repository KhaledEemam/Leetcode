class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        longest = 0
        length = 0
        
        for num in nums :
            if (num -1) not in nums_set :
                length = +1
                while (1+num) in nums_set :
                    length += 1
                    num += 1
                
                longest = max(length,longest)
                
        return longest
        