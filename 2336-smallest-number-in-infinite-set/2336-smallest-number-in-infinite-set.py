import heapq

class SmallestInfiniteSet:

    def __init__(self):
        self.set = set()
        self.heap = list(self.set)
        heapq.heapify(self.heap)
        self.smallest = 0
        

    def popSmallest(self) -> int:
        if self.heap :
            smallest_heap = heapq.heappop(self.heap)
            if smallest_heap < self.smallest + 1  :
                self.set.remove(smallest_heap)
                return smallest_heap
                
            elif smallest_heap > self.smallest + 1 :
                heapq.heappush(self.heap,smallest_heap)
                self.smallest += 1
                return self.smallest
            
            else :
                self.set.remove(smallest_heap)
                self.smallest += 1
                return self.smallest
        else :
            self.smallest += 1
            return self.smallest
            
    def addBack(self, num: int) -> None:
        if num not in self.set :
            self.set.add(num)
            heapq.heappush(self.heap,num)
            return
        return


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)