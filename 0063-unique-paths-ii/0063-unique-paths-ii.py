class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        """
        for i in range(len(obstacleGrid)) :
            for k in range(len(obstacleGrid[0])) :
                           if obstacleGrid[i][k] == 1 :
                            obstacleGrid[i][k] = -1
                         
        rows , cols = len(obstacleGrid) , len(obstacleGrid[0])
        cache = [[0]*cols for i in range(rows)]
        
        def move(x,y) :
            if x == rows or y == cols :
                return 0
            if obstacleGrid[x][y] == -1 :
                return 0
            if x == rows -1 and y == cols - 1 :
                return 1
            if cache[x][y] > 0 :
                return cache[x][y]
            
            cache[x][y] = move(x+1,y) + move(x,y+1)
            return cache[x][y]
        
        return move(0,0)
        """
        for i in range(len(obstacleGrid)) :
            for k in range(len(obstacleGrid[0])) :
                if obstacleGrid[i][k] == 1 :
                    obstacleGrid[i][k] = -1
                            
        rows , cols = len(obstacleGrid) , len(obstacleGrid[0])
        prevrow = [0] * (cols - 1) + [1]
        
    #    if obstacleGrid[0][0] == -1 or obstacleGrid[rows-1][cols-1] == -1 :
    #       return 0
        
        
        for row_no in range(rows-1,-1,-1) :
            currow = obstacleGrid[row_no]
            for col_no in range(cols-1,-1,-1) :
                if currow[col_no] == -1 :
                    currow[col_no] = 0
                elif col_no+1 > cols-1 :
                    currow[col_no] = prevrow[col_no]
                else :
                    currow[col_no] = currow[col_no+1] + prevrow[col_no]
                    
            prevrow = currow
            
            
        return prevrow[0]