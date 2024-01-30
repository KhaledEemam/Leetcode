class Solution:
    def jump(self, nums: List[int]) -> int:
        goal = len(nums) -1
        steps = 0
        
        def backward_jump(goal,steps) :
            if goal == 0 :
                return steps
            
            min_steps = []

            for i in range(goal-1,-1,-1) :
                if i + nums[i] >= goal :
                    min_steps.append(i)

            goal = min(min_steps)
            steps += 1
            return backward_jump(goal,steps)
        
        return backward_jump(goal,steps)

        