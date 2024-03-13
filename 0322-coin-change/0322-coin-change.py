class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float("inf")] * (amount+1)
        dp[0] = 0
        for i in range(amount+1) :
            for coin in coins :
                if i-coin >= 0 :
                    dp[i] = min(dp[i],(1 + dp[i-coin]))
                
        return dp[amount] if dp[amount] != float("inf") else -1
        
        """
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
        """