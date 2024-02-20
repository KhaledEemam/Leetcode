class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0 : return 0
        
        i = 0
        
        while x > i * i :
            i += 1
            
        
        if (i*i) > x  :
            return i -1
        else :
            return i
            