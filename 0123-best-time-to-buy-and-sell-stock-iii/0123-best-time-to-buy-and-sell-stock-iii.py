class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left_profit = [0] * len(prices)
        right_profit = [0] * len(prices)
        
        min_left = prices[0]
        max_left_profit = float("-inf")
        for i in range(1,len(prices)) :
            max_left_profit = max(max_left_profit,(prices[i]-min_left))
            left_profit[i] = max_left_profit
            if prices[i] < min_left :
                min_left = prices[i]
                
        max_right = prices[-1]
        max_right_profit = float("-inf")
        for i in range(len(prices)-2,-1,-1) :
            max_right_profit = max(max_right_profit,(max_right-prices[i]))
            right_profit[i] = max_right_profit
            if prices[i] > max_right :
                max_right = prices[i]
                
        two_trans_profits = right_profit[0]
        for i in range(1,len(prices)) :
            two_trans_profits = max(0,two_trans_profits,(left_profit[i-1]+right_profit[i]))
            
        return two_trans_profits
        
        
        """
        # O(n^2)
        def get_max(sub_list) :
            cur_prof = float("-inf")
            min_start = float("inf")

            if len(sub_list) < 2 :
                return 0

            for i in range(len(sub_list)) :
                cur_prof = max(0,cur_prof,(sub_list[i]-min_start))
                if sub_list[i] < min_start :
                    min_start = sub_list[i]

            return cur_prof
    
        max_prof = float("-inf")
        for i in range(len(prices)) :
            list_1 = prices[:i]
            list_2 = prices[i:]

            prof = get_max(list_1) + get_max(list_2)
            if prof > max_prof :
                max_prof = prof

        return max_prof
        """