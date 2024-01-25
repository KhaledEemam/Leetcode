class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        q = collections.deque()
        visit = set()
        rows , columns = len(grid) , len(grid[0])
        
        q.append((0,0))
        visit.add((0,0))
        if grid[0][0] == 0 :
            length = 1
        else :
            return -1
        
        while q :
            for i in range(len(q)) :
                row , column = q.popleft()
                
                if row == rows -1 and column == columns -1 :
                    return length
                
                directions = [[1,0],[-1,0],[0,1],[0,-1],
                              [1,1],[-1,-1],[-1,1],[1,-1]]
                
                for r , c in directions :
                    dr , dc = r + row , c + column
                    if dr not in range(rows) or dc not in range(columns) or (dr,dc) in visit or grid[dr][dc] == 1 :
                        continue
                    visit.add((dr,dc))
                    q.append((dr,dc))
                    
            length += 1
                    
        return -1
                
                