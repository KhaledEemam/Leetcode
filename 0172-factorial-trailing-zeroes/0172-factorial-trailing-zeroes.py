class Solution:
    def trailingZeroes(self, n: int) -> int:
        k = 0
        num = n
        res = 0
        
        while num/5 >= 1 :
            k += 1
            res += num // 5
            num = num / 5
            
        return int(res)
            
            
            
            
        