class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows , columns = len(grid) , len(grid[0])
        visit = set()
        max_areas = 0
        
        def bfs(r,c) :
            count = 1
            q = collections.deque()
            q.append((r,c))
            visit.add((r,c))
            
            while q :
                row , column = q.popleft()
                directions = [[1,0],[-1,0],[0,1],[0,-1]]
                for dr,dc in directions :
                    r , c = row+dr , column+dc
                    if (r in range(rows) and c in range(columns) and grid[r][c] == 1 and (r,c) not in visit) :
                        visit.add((r,c))
                        q.append((r,c))
                        count += 1
                    
            
            
            return count
            
        for i in range(rows) :
            for n in range(columns) :
                if grid[i][n] == 1 and (i,n) not in visit :
                    max_areas = max(max_areas,bfs(i,n)) 
        
        
        return max_areas