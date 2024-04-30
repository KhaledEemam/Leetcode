class StockSpanner:

    def __init__(self):
        self.prices = []
        self.spans = {}
        

    def next(self, price: int) -> int:
        span = 1
        i = len(self.prices) - 1
        while i >= 0 and self.prices[i] <= price :
            span += self.spans[i]
            i = i - self.spans[i]
        
        self.prices.append(price)
        
        self.spans[len(self.prices) - 1] = span
        return span
        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)