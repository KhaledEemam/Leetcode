class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # dp
        dp = [[0] * (n+1) for i in range(m+1) ]
        ROWS , COLUMNS = len(dp) , len(dp[0])
        dp[ROWS-2][COLUMNS-1] = 1
        
        for i in range(ROWS-2,-1,-1) :
            for k in range(COLUMNS-2,-1,-1) :
                dp[i][k] = dp[i+1][k] + dp[i][k+1]
                
        return dp[0][0]
        
        
        
        """
        ROWS , COLUMNS = m , n
        paths = 0
        memo = {}
        visited = set()
        
        def dfs(x,y) :
            if x < 0 or x > ROWS-1 or y < 0 or y > COLUMNS-1  :
                return 0

            if x == ROWS-1 and y == COLUMNS -1 :
                return 1
            
            if (x,y) in memo :
                return memo[(x,y)]
            
            
            paths = dfs(x+1,y) + dfs(x,y+1)
            memo[(x,y)] = paths
            
            return paths
        
        return dfs(0,0)
        """