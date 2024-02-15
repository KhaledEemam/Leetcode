class Solution:
    def isHappy(self, n: int) -> bool:
        
        def get_digits(n):
            output = 0
            while n :
                digit = n % 10
                digit = digit**2
                output += digit
                n = n//10
            return output
        
        nums_set = set()
        digits_sum = 0 
        
        while digits_sum not in nums_set :
            digits_sum = get_digits(n)
            if digits_sum == 1 :
                return True
            nums_set.add(n)
            n = digits_sum
            
            
        return False
        