class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        if len(nums) < 3 : return False
        num1 , num2 , num3 = nums[0] , float("inf") , float("inf")
        
        for i in range(1,len(nums)) :
            if nums[i] <= num1 :
                num1 = nums[i]
            elif nums[i] <= num2 :
                num2 = nums[i]
            else :
                return True
            
        return False
        
        
        """
        if len(nums) < 3 :
            return False
        
        is_greater_left = [False] * len(nums)
        is_greater_right = [False] * len(nums)
        
        min_left = nums[0]
        max_right = nums[-1]
        
        for i in range(1,len(nums)) :
            if nums[i] > min_left :
                is_greater_left[i] = True
            else :
                min_left = min(min_left,nums[i])
                
        for i in range(len(nums)-2,-1,-1) :
            if nums[i] < max_right :
                is_greater_right[i] = True
            else :
                max_right = max(max_right,nums[i])
                
        for i in range(len(nums)) :
            if is_greater_left[i] and is_greater_right[i] :
                return True
            
        return False
        """        
                
            
            
