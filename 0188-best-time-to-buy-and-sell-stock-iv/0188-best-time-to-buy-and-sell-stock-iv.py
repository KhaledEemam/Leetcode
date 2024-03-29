class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        dp = [[0] * len(prices) for i in range(k+1)]
        max_diff = float("-inf")

        for i in range(1,k+1) :
            max_diff = float("-inf")
            for j in range(1,len(prices)) :
                max_diff = max(max_diff,dp[i-1][j-1] - prices[j-1])
                dp[i][j] = max(dp[i][j-1] , max_diff + prices[j])

        print(dp)
        return dp[k][len(prices)-1]
                
        
        """
        # states : bought , no_state
        memo = {}
        
        def get_max_profit(index,bought,transaction) :
            if index >= len(prices) or transaction == k :
                return 0
            
            if (index,bought,transaction) in memo :
                return memo[(index,bought,transaction)]
            
            p1 , p2 = 0 , 0
            if bought is not None :
                # bought_sell
                p1 = (prices[index] - bought) + get_max_profit(index+1,None,transaction+1)
                # bought_skip
                p2 = get_max_profit(index+1,bought,transaction)
            
            else :
                # no_state_skip         
                p1 = get_max_profit(index+1,bought,transaction)
                # no_state_buy  
                p2 = get_max_profit(index+1,prices[index],transaction)
                
            max_profit = max(p1,p2)
            memo[(index,bought,transaction)] = max_profit
            return max_profit
        
        
        return get_max_profit(0,None,0)
        """