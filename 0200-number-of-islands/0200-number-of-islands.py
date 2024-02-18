class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows , columns = len(grid) , len(grid[0])
        visited = set()
        
        def dfs(r,c) :
            if r < 0 or c < 0 or r== rows or c == columns or grid[r][c] == "0"or (r,c) in visited :
                return False
            
            visited.add((r,c))
            
            dfs(r+1,c)
            dfs(r-1,c)
            dfs(r,c+1)
            dfs(r,c-1)
            
            return True
        
        count = 0
        for row in range(rows) :
            for column in range(columns) :
                if dfs(row,column) :
                    count += 1
        
        return count
                
            
        
                    
                
        
            
        