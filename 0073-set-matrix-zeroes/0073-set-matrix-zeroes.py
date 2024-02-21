class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        
        rows , columns = len(matrix) , len(matrix[0])
        rows_set = set()
        column_set = set()
        
        for i in range(rows) :
            for j in range(columns) :
                if matrix[i][j] == 0 :
                    rows_set.add(i)
                    column_set.add(j)
                    
        for i in rows_set :
            for j in range(columns) :
                matrix[i][j] = 0
                
        
        for i in range(rows) :
            for j in column_set :
                matrix[i][j] = 0
                
                
        
            
        