class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        ROWS , COLUMNS = m , n
        paths = 0
        memo = {}
        visited = set()
        
        def dfs(x,y) :
            if x < 0 or x > ROWS-1 or y < 0 or y > COLUMNS-1 or (x,y) in visited :
                return 0

            if x == ROWS-1 and y == COLUMNS -1 :
                return 1
            
            if (x,y) in memo :
                return memo[(x,y)]
            
            visited.add((x,y))
            
            paths = dfs(x+1,y) + dfs(x,y+1)
            
            visited.remove((x,y))
            memo[(x,y)] = paths
            
            return paths
        
        return dfs(0,0)
                
        