class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        l = len(digits) -1 
        remaining = 1
        
        while l >= 0 and remaining > 0 :
            digits[l] += remaining
            remaining = digits[l] // 10
            digits[l] = digits[l] % 10
            l -= 1
            
        if remaining > 0 :
            digits = [1] + digits
            
        return digits
                 
         