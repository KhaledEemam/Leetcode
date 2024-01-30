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
            
            
        """
        profits = []
        for i in range(len(prices)-1) :
            cur = prices[i]prices[i] - 
            max_number = cur
            for index in range(i+1,len(prices)) :
                if prices[index] > max_number :
                    max_number = prices[index]
            profit = max_number - cur
            profits.append(profit)
           
        if len(prices) > 1 :
            return max(profits)
        else :
            return 0
           """     
                
            
            
        