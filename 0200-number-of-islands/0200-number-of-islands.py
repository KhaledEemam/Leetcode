class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid :
            return 0
        
        rows , columns = len(grid) , len(grid[0])
        visit = set()
        isalnds = 0
        
        def bfs(r,c) :
            q = collections.deque()
            visit.add((r,c))
            q.append((r,c))
            
            while q :
                row,column = q.popleft()
                directions = [[1,0],[-1,0],[0,1],[0,-1]]

                for dr , dc in directions :
                    r , c = row+dr , column+dc
                    if ((r,c) not in visit and r in range(rows) and c in range(columns) and grid[r][c] == "1")  :
                        q.append((r,c))
                        visit.add((r,c))
            
        for r in range(rows) :
            for c in range(columns) :
                if (r,c) not in visit and grid[r][c] == "1" :
                    bfs(r,c)
                    isalnds += 1
                    
        return isalnds
                    
                
        
            
        