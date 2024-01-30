class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 1 :
            return 0
        
        profits = []
        for i in range(len(prices)-1) :
            profit = prices[i+1] -  prices[i]
            profits.append(profit)
            
        max_profit = 0    
        for profit in profits :
            if profit > 0 :
                max_profit += profit
                
        return max_profit
                
        