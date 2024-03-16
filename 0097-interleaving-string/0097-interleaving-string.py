class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3) : return False
        
        dp = [[False] * (len(s1)+1) for i in range(len(s2)+1)]
        dp[-1][-1] = True
        
        for r in range(len(dp)-1,-1,-1):
            for c in range(len(dp[r])-1,-1,-1):
                if c < len(s1) and s3[r+c] == s1[c] and dp[r][c+1] == True :
                    dp[r][c] = True
                if r < len(s2) and s3[r+c] == s2[r] and dp[r+1][c] == True :
                    dp[r][c] = True
                    
        return dp[0][0]
                
        
        
        
        """
        # DFS
        memo = {}
        
        def dfs(l,r) :
            if l == len(s1) and r == len(s2) :
                return True
            
            if (l,r) in memo :
                return memo[(l,r)]
            
            if l < len(s1) and s1[l] == s3[l+r] and dfs(l+1,r):
                return True
            
            if r < len(s2) and s2[r] == s3[l+r] and dfs(l,r+1) :
                return True
            
            memo[(l,r)] = False
            return False
        
        if len(s1) + len(s2) != len(s3) :
            return False
        else :
            return dfs(0,0)
            """