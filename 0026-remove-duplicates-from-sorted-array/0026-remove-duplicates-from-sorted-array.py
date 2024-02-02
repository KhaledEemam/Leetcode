class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        j = 1 
        for i in range(1,len(nums)) :
            if nums[i] == nums[j-1] :
                pass
            else :
                nums[j] = nums[i]
                j += 1
        
        return j
        """   
    my_hash = {}
        j = 0 
        
        for num in nums :
            if num in my_hash :
                pass
            else :
                my_hash[num] = 1
                nums[j] = num
                j += 1
                
        return j
        """
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
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