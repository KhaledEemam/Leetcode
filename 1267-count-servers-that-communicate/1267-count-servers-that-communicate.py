class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        rows , columns = len(grid) , len(grid[0])
        rowsCount , columnsCount = [0] * rows , [0] * columns

        for r in range(rows) :
            for c in range(columns) :
                if grid[r][c] :
                    rowsCount[r] += 1
                    columnsCount[c] += 1

        answer = 0
        for r in range(rows) :
            for c in range(columns) :
                if grid[r][c] and max(rowsCount[r] , columnsCount[c]) > 1 :
                    answer += 1

        return answer