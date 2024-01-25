class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows , columns = len(grid) , len(grid[0])
        st_point = None
        visit = set()
        minutes , fresh = 0 , 0
        q = collections.deque()
        for row in range(len(grid)) :
            for column in range(len(grid[0])) :
                if grid[row][column] == 2 :
                    visit.add((row,column))
                    q.append((row,column))
                    st_point = (row,column)
                elif grid[row][column] == 1 :
                    fresh += 1

        
        if st_point  :              
            while q and fresh > 0:
                for i in range(len(q)) :
                    r , c = q.popleft()
                    directions = [[1,0],[-1,0],[0,1],[0,-1]]
                    for row , column in directions :
                        dr , dc = row+r , column + c
                        if (dr not in range(rows) or dc not in range(columns) or (dr,dc) in visit or grid[dr][dc] == 0):
                            continue

                        q.append((dr,dc))
                        visit.add((dr,dc))
                        grid[dr][dc] = 2
                        fresh -= 1

                minutes += 1
        
        for row in range(len(grid)) :
            for column in range(len(grid[0])) :
                if grid[row][column] == 1 :
                    return -1
            
        return minutes
                