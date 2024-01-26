class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        cache = [[0]*n for i in range(m)]
        
        def move(x,y,m,n) :
            if x > m-1 or y > n-1 :
                return 0
            if x == m-1 and y == n-1 :
                return 1
            if cache[x][y] > 0 :
                return cache[x][y]
            
            cache[x][y] = move(x+1,y,m,n) + move(x,y+1,m,n)
            return cache[x][y]
        
        return move(0,0,m,n)
            
            
            