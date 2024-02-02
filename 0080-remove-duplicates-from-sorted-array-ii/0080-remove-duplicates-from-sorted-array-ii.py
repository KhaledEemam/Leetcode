class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        j = 1
        count = 1
        
        for i in range(1,len(nums)) :
            if (nums[i] == nums[j-1]) and count < 2 :
                nums[j] = nums[i]
                j += 1
                count += 1
            elif nums[i] != nums[j-1] :
                nums[j] = nums[i]
                count = 1
                j += 1
                
        return j
                
                
        """
        l , r = 0 , 0
        while r < len(nums) :
            count = 1 
            while (((r+1) < len(nums)and(nums[r] == nums[r+1]))) :
                count += 1 
                r += 1 
            
            for i in range(min(2,count)) :
                nums[l] = nums[r]
                l += 1
            
            r+= 1
            
        return l      
                
   #################################################################################     
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
           """         