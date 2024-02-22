class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        original | state | output
            0    |    0  |    0
            1    |    0  |    1
            0    |    1  |    2
            1    |    1  |    3
        """
        rows , columns = len(board) , len(board[0])
        
        def get_nei(r,c) :
            nei = 0
            for i in range(r-1,r+2):
                for j in range(c-1,c+2) :
                    if (i == r and j == c) or i < 0 or j< 0 or i >= rows or j >= columns :
                        continue
                    if board[i][j] in [1,3] :
                        nei += 1
            
            return nei
        
        
        
        for k in range(rows) :
            for v in range(columns) :
                nei = get_nei(k,v)
                if board[k][v] == 1 :
                    if nei in [2,3] :
                        board[k][v] = 3
                else :
                    if nei == 3 :
                        board[k][v] = 2
        
        for k in range(rows) :
            for v in range(columns) :
                if board[k][v] == 1 :
                    board[k][v] = 0
                elif board[k][v] in [2,3] :
                    board[k][v] = 1
                    
                    
                
                    
                
                        
                    
        