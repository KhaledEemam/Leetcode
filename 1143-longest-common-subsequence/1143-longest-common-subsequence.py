class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = [[0] * (len(text1)+1) for i in range(len(text2)+1)]
        n , m = len(text1)+1 , len(text2)+1
        
        for i in range(m-2,-1,-1) :
            for k in range(n-2,-1,-1) :
                if text1[k] == text2[i] :
                    dp[i][k] = 1 + dp[i+1][k+1]
                else :
                    dp[i][k] = max(dp[i+1][k],dp[i][k+1])

        return(dp[0][0])
                    
                    
            
        
        