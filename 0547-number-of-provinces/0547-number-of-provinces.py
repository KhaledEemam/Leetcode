class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        ROWS , COLUMNS = len(isConnected) , len(isConnected[0])
        visited = set()
        provinces = 0
        
        def dfs(start) :
            visited.add(start)
            for end in range(COLUMNS) :
                if isConnected[start][end] == 1 and end not in visited :
                    dfs(end)
        
        for start in range(ROWS) :
            if start not in visited :
                provinces += 1
                dfs(start)
                
        return provinces
                
                    
                
            
        
                