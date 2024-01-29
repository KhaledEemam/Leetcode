class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        j = 0 
        my_hash = {}
        
        for num in nums :
            if num not in my_hash :
                nums[j] = num
                my_hash[num] = 1
                j += 1
            elif ((num in my_hash) & (my_hash[num] < 2)) :
                nums[j] = num
                my_hash[num] += 1
                j += 1
                
        return j
                
                