class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        adj = collections.defaultdict(list)
        
        for i , eq in enumerate(equations) :
            a , b = eq
            adj[a].append([b,values[i]])
            adj[b].append([a, 1 / values[i] ])
            
            
        
        def dfs(src,target) :
            if src not in adj or target not in adj :
                return -1
            queue , visit = collections.deque() , set()
            queue.append((src,1))
            visit.add(src)
            
            while queue :
                s , w = queue.popleft()
                if s == target :
                    return w
                for adjacent , weight in adj[s] :
                    if adjacent not in visit :
                        visit.add(adjacent)
                        queue.append([adjacent,w*weight])
            
            return -1
        
        
        return [dfs(q[0],q[1]) for q in queries]
            
            
        