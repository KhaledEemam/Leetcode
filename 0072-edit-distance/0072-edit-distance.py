class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        dp = [[float("inf")] * (len(word1)+1) for i in range(len(word2) + 1)]
        ROWS , COLUMNS = len(dp) , len(dp[0])
        
        for i in range(ROWS) :
            dp[i][COLUMNS-1] = ROWS - i -1 
            
        for j in range(COLUMNS) :
            dp[ROWS-1][j] = COLUMNS - j -1
            
        
        for r in range(ROWS-2,-1,-1) :
            for c in range(COLUMNS-2,-1,-1) :
                if word1[c] == word2[r] :
                    dp[r][c] = dp[r+1][c+1]
                else :
                    dp[r][c] = 1 + min(dp[r+1][c+1],dp[r+1][c],dp[r][c+1])
                    
        return dp[0][0]