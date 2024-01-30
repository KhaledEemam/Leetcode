class Solution:
    def canJump(self, nums: List[int]) -> bool:
        cache = {}
        def add_steps(i,steps) :
            if steps >= len(nums) - 1 :
                return True
            elif i >= len(nums) :
                return False

            max_steps = nums[i]

            for step in range(1,max_steps+1) :
                if (i+step) in cache :
                    if cache[i+step] :
                        return True
                else :
                    cache[i+step] = add_steps(i+step,steps+step)
                    if cache[i+step] :
                        return True

            return False

        return add_steps(0,0)
        
        """ 
        def can_reach_end(i, steps):
            if steps >= len(nums) - 1:
                return True
            if i >= len(nums):
                return False
            
            max_steps = min(len(nums) - 1 - i, nums[i])  
            for step in range(max_steps, 0, -1):  
                if can_reach_end(i + step, steps + step):  
                    return True
            
            return False
        
        return can_reach_end(0, 0)
        """
        
                
        
            
            
            
            
        