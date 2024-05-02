class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        queue = deque()
        visited = set()
        ROWS, COLUMNS = len(grid) , len(grid[0])
        minutes = 0
        fresh = 0
        
        for row in range(ROWS) :
            for column in range(COLUMNS) :
                if grid[row][column] == 2 :
                    visited.add((row,column))
                    queue.append((row,column))
                elif grid[row][column] == 1 :
                    fresh += 1
                    
        if fresh > 0 :
            while queue and fresh > 0 :

                for i in range(len(queue)) :
                    x , y = queue.popleft()
                    directions = [[1,0],[0,1],[-1,0],[0,-1]]

                    for direction in directions :
                        dx , dy = direction
                        new_x , new_y = x+dx , y+dy

                        if new_x < 0 or new_x >= ROWS or new_y < 0 or new_y >= COLUMNS or (new_x,new_y) in visited :
                            continue

                        if grid[new_x][new_y] == 1  :
                            visited.add((new_x,new_y))
                            grid[new_x][new_y] = 2
                            queue.append((new_x,new_y))
                            fresh -= 1


                minutes += 1
          
        for row in range(ROWS) :
            for column in range(COLUMNS) :
                if grid[row][column] == 1 :
                    return -1
        
        return minutes