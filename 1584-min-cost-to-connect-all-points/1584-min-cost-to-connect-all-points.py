class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        adj = {i : [] for i in range(n)}
        
        for i in range(n) :
            x1 , y1 = points[i]
            for j in range(i+1,n) :
                x2 , y2 = points[j]
                distance = abs(x2-x1) + abs(y2-y1)
                adj[i].append([distance , j])
                adj[j].append([distance , i])
        
        visited = set()
        heap = [[0,0]]
        res = 0

        while len(visited) < n :
            cost , point = heapq.heappop(heap)
            if point in visited : 
                continue
            
            visited.add(point)
            res += cost

            for distance,node in adj[point] :
                if node not in visited :
                    heapq.heappush(heap,[distance,node])
        
        return res


