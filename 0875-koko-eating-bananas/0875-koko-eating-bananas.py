import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        def check_speed(speed) :
            hours = 0
            for pile in piles :
                hours += math.ceil(pile/speed)
                
            return hours
        
        
        l , r = 1 , max(piles)
        result = r
        
        while r >= l :
            m = (l+r) // 2
            
            cur_hours = check_speed(m)
            
            if cur_hours > h :
                l = m + 1
            else :
                result = m
                r = m - 1
                
        return result
                
            
        