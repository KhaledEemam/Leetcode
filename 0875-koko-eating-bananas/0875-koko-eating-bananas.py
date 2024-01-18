import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def check_number(num) :
            my_calc_hours = 0
            for pile in piles :
                my_calc_hours += math.ceil(pile/num)

            if my_calc_hours > h :
                return -1 
            else :
                return num

        def get_num(l,r) :
            l = l
            r = r
            result = r
            while r >= l :
                m = (r+l) // 2
                if check_number(m) == -1 :
                    l = m + 1
                else :
                    result = min(result,check_number(m))
                    r = m - 1

            return result
    

        l = 1
        r = max(piles)
        max_possible_num =  get_num(l,r)

        return max_possible_num
            
                
            
            
        