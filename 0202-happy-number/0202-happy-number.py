class Solution:
    def isHappy(self, n: int) -> bool:
        
        def get_digits(string):
            digits = []
            result = 0
            for char in string:
                digits.append(int(char))
            result = sum(digit**2 for digit in digits)
            return result
        
        my_hash = {}
        digits_sum = 0 
        
        while digits_sum not in my_hash :
            digits_sum = get_digits(str(n))
            if digits_sum == 1 :
                return True
            my_hash[n] = 0
            n = digits_sum
            
            
        return False
        