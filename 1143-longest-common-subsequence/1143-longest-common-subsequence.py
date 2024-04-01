class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = [[0] * (len(text1)+1) for i in range(len(text2)+1)]
        
        rows = len(dp)
        columns = len(dp[0])
        
        for i in range(rows-2,-1,-1):
            for k in range(columns-2,-1,-1) :
                if text2[i] == text1[k] :
                    dp[i][k] = 1 + dp[i+1][k+1]
                else :
                    dp[i][k] = max(dp[i][k+1],dp[i+1][k])
                    
        return dp[0][0]
            
        
        