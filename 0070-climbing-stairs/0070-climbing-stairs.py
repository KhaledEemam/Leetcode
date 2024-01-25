class Solution:
    def climbStairs(self, n: int) -> int:
        """
        if n <= 3 :
            return n
        
        return self.climbStairs(n-1) + self.climbStairs(n-2)
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

        