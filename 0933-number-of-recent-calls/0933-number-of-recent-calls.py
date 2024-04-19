class RecentCounter:

    def __init__(self):
        self.requests = []
        

    def ping(self, t: int) -> int:
        self.requests.append(t)
        left_border = t - 3000
        count = 0
        for request in self.requests :
            if request >= left_border:
                count += 1
        return count
            
        


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)