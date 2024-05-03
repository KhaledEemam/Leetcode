class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        next_cost , after_next_cost = 0 , 0
        
        for i in cost :
            cur_cost = i + min(next_cost,after_next_cost)
            temp = next_cost
            next_cost = cur_cost
            after_next_cost = temp
            
        return min(next_cost,after_next_cost)
            
        