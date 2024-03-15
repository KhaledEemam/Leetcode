class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        
        memo = collections.defaultdict(list)
        min_sum = float("inf")
        ROWS = len(triangle)
        
        def dfs_sum(r,k):
            if r == ROWS :
                return 0
            if (r,k) in memo :
                return memo[(r,k)]
            
            cur_sum = triangle[r][k] + min(dfs_sum(r+1,k) , dfs_sum(r+1,k+1))
            
            memo[(r,k)] = cur_sum
            return cur_sum
        
        return dfs_sum(0,0) 
                
        """
        
        dp = [0] * (len(triangle)+1)
        for row in triangle[::-1] :
            for i , n in enumerate(row) :
                dp[i] = n + min(dp[i],dp[i+1])
                
        return dp[0]
        """ 
        