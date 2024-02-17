class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = {i : [] for i in range(9)}
        col = {i : [] for i in range(9)}
        cubes = {tuple([l,r]) : [] for l in range(3) for r in range(3)}
        
        def get_cube_num(index) :
            if index >= 0 and index < 3 :
                return 1
            if index >= 3 and index < 6 :
                return 2
            if index >= 6 and index < 9 :
                return 3
            
        for r in range(len(board)) :
            for c in range(len(board[0])) :
                if board[r][c] == "." :
                    pass
                else :
                    cube_row = get_cube_num(r)
                    cube_column = get_cube_num(c)
                    key = tuple([cube_row-1,cube_column-1])

                    if board[r][c] in rows[r] or board[r][c] in col[c] or board[r][c] in cubes[key] :
                        return False
                    rows[r].append(board[r][c])
                    col[c].append(board[r][c])
                    cubes[key].append(board[r][c])
                    
        
        return True