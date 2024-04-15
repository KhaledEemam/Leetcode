class Solution:
    def tribonacci(self, n: int) -> int:
        
        mono = {}
        
        def backtrack(number) :
            if number == 2 :
                return 1
            
            if number <= 1 :
                return number
            
            if number in mono :
                return mono[number]
            
            value = backtrack(number-1) + backtrack(number-2) + backtrack(number-3)
            
            mono[number] = value
            
            return value
        
        
        return backtrack(n)
        