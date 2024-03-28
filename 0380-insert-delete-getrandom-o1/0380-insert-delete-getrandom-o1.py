import random

class RandomizedSet:

    def __init__(self):
        self.rset = {}
        self.numlist = []
        

    def insert(self, val: int) -> bool:
        if val in self.rset :
            return False
        else :
            self.rset[val] = len(self.numlist)
            self.numlist.append(val)
            return True
            

    def remove(self, val: int) -> bool:
        if val not in self.rset :
            return False
        else :
            lastval = self.numlist[-1]
            idx = self.rset[val]
            self.numlist[idx] = lastval
            self.numlist.pop()
            self.rset[lastval] = idx
            del self.rset[val]
            
            return True
        

    def getRandom(self) -> int:
        return random.choice(self.numlist)
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()