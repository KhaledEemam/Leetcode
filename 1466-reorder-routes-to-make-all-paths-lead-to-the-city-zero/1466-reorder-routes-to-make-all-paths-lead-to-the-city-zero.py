class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        edges ={ (connection[0],connection[1]) for connection in connections }
        neighbors = {city : [] for city in range(n) }
        for connection in connections :
            a , b = connection
            neighbors[a].append(b)
            neighbors[b].append(a)
            
            
        visited = set()
        changes = 0
        def dfs(city) :
            nonlocal edges,neighbors,visited,changes
            
            for neighbor in neighbors[city] :
                if neighbor in visited :
                    continue
                
                if (neighbor,city) not in edges :
                    changes += 1
                    
                visited.add(neighbor)
                dfs(neighbor)


        visited.add(0)
        dfs(0)
        return changes
                    
                    
                    
                    
