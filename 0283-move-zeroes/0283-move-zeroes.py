class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k , zeros = 0 , 0 
        for i in range(len(nums)) :
            if nums[i] != 0 :
                nums[k] = nums[i]
                k += 1
            else :
                zeros += 1
                
        nums[len(nums)-zeros:] = [0] * zeros
                
                
                
        
                
        