class Solution:
    def tribonacci(self, n: int) -> int:
        n0 , n1 , n2 = 0 , 1 , 1
        
        if n <= 1 :
            return n
        if n == 2 :
            return 1
        
        for i in range(3,n+1) :
            value = n0 + n1 + n2
            n0 = n1
            n1 = n2
            n2 = value
            
        return value
        
        """
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
        """