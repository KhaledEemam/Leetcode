class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 1 :
            return 0
        
        l  = 0
        max_profit = 0
        
        for i in range(1,len(prices)) :
            if prices[i] < prices[l] :
                l = i
            elif prices[i] > prices[l] :
                max_profit = max(max_profit,prices[i] - prices[l])
                    
        return max_profit