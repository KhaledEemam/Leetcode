class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l , r = 0 , len(nums) - 1
        
        while r >= l :
            m = (r+l) // 2
            
            if nums[m] == target :
                return m
            
            # left portion
            if nums[m] >= nums[l] :
                if nums[m] < target or target < nums[l]:
                    l = m + 1
                elif nums[m] > target :
                    r = m - 1
            
            # right portion
            else :
                if nums[m] > target or target > nums[r] :
                    r = m - 1
                elif nums[m] < target :
                    l = m + 1
                    
        
        return -1