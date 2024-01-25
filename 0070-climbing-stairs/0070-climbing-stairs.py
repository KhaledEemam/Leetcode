class Solution:
    def climbStairs(self, n: int) -> int:
        """
        cache = {}
        def memoization(n) :
            if n <= 3 :
                return n
            if n in cache :
                return cache[n]
            
            cache[n] = memoization(n-1) + memoization(n-2)
            return cache[n]
        
        return memoization(n)
        """
      
        cache = {}
        def memo(i) :
            if i == n :
                return 1
            if i > n :
                return 0
            if i in cache :
                return cache[i]
            
            cache[i] = memo(i+1) + memo(i+2)
            return cache[i]
        
        return memo(0)
        
        


        