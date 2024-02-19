class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        length = len(board)
        
        board.reverse()
        def intpos(square) :
            r = (square -1) // length 
            c = (square - 1) % length
            if r %2 :
                c = length -1 - c
            return r,c
        
        queue = deque()
        queue.append([1,0]) # square , moves
        visited = set()
        
        while queue :
            
            square , moves = queue.popleft()
            
            for i in range(1,7) :
                new_square = square + i 
                r , c = intpos(new_square)
                if board[r][c] != -1 :
                    new_square = board[r][c]
                if new_square == length * length :
                    return moves +1 
                if new_square not in visited :
                    visited.add(new_square)
                    queue.append([new_square,moves+1])
                    
        return -1
                
            
            
            