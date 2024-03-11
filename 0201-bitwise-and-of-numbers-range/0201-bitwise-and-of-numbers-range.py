class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        res = 0
        
        for i in range(32) :
            l = (left >> i)  & 1
            
            if not l :
                continue
            
            remain = left % (1 << (i+1))
            diff = (1 << (i+1)) - remain
            
            if (right - left) < diff :
                res = res | (l << i)
                
        return res
            
            
            
            
            
        """i = 0
        while left != right :
            left = left >> 1
            right = right >> 1
            i += 1
            
        return left << i"""
            