class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """ 
        rows , columns = len(board) , len(board[0])
        
        def dfs(r,c) :
            if r < 0 or r == rows or c < 0 or c == columns or board[r][c] != "O" :
                return
            
            board[r][c] = "T"
            
            dfs(r+1,c)
            dfs(r-1,c)
            dfs(r,c+1)
            dfs(r,c-1)
            
        for row in range(rows) :
            for column in range(columns) :
                if (row in [0,rows-1] or column in [0,columns-1]) and board[row][column] == "O" :
                    dfs(row,column)
                    
                    
        for row in range(rows) :
            for column in range(columns) :
                if board[row][column] == "O" :
                    board[row][column] = "X"
                    
        for row in range(rows) :
            for column in range(columns) :
                if  board[row][column] == "T" :
                    board[row][column] = "O"
                    
            
            
            