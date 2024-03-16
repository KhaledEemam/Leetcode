class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        memo = {}
        
        def dfs(l,r) :
            if l + r == len(s3) :
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
        
                