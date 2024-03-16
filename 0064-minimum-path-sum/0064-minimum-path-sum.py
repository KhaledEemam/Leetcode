class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        ROWS , COLUMNS = len(grid) , len(grid[0])
        matrix = [[float("inf")] * (COLUMNS+1) for r in range(ROWS+1)]
        matrix[ROWS][COLUMNS-1] = 0
        
        for r in range(ROWS-1,-1,-1):
            for c in range(COLUMNS-1,-1,-1) :
                matrix[r][c] = grid[r][c] + min(matrix[r+1][c],matrix[r][c+1])
                
        return matrix[0][0]
        

        """
        # dfs
        memo = {}
        ROWS , COLUMNS = len(grid) , len(grid[0])
        visited = set()
        
        def min_path_sum(r,c) :
            if r >= ROWS or c >= COLUMNS or r < 0 or c < 0 or (r,c) in visited :
                return float("inf")
            
            if r == ROWS -1 and c == COLUMNS -1 :
                return grid[r][c]
            
            if (r,c) in memo :
                return memo[(r,c)]
            
            visited.add((r,c))
            
            cur_sum = grid[r][c] + min(min_path_sum(r+1,c), min_path_sum(r,c+1))
            memo[(r,c)] = cur_sum
            
            visited.remove((r,c))
            
            return cur_sum
        
        return min_path_sum(0,0)
        """
        