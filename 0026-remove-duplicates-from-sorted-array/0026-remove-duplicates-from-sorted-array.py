class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:        
        i = 0
        k = 0
        while i < len(nums) :
            while i+1 < len(nums) and nums[i] == nums[i+1] :
                i += 1
                
            nums[k] = nums[i]
            k += 1
            i += 1
            
        return k
                
            
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        """
        j = 1
        for i in range(1,len(nums)) :
            if nums[i] == nums[i-1] : 
                pass
            else :
                nums[j] = nums[i]
                j = j+1
                
        return j
        """