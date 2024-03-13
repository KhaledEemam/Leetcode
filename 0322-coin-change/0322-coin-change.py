class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}
        
        def get_steps(amt) :
            if amt == 0 : return 0
            if amt <= 0 : return float("inf")
            
            if amt in memo : return memo[amt]
            
            steps = float("inf")
            
            for coin in coins :
                steps = min(steps,1+get_steps(amt-coin))
                
            memo[amt] = steps
            
            return steps
        
        min_steps = get_steps(amount)
        return min_steps if min_steps != float("inf") else -1