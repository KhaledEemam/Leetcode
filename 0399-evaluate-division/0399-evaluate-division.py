class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        adj = defaultdict(list)
        for i , eq in enumerate(equations) :
            a , b = eq
            adj[a].append([b,values[i]])
            adj[b].append([a,1/values[i]])
            
        
        def bfs(src,target) :
            if src not in adj or target not in adj :
                return -1
            
            queue , visit = deque() , set()
            queue.append((src,1))
            visit.add(src)
            
            while queue :
                
                s , w = queue.popleft()

                for t , weight in adj[s] :
                    
                    if t == target :
                        return w * weight
                    
                    if t not in visit :
                        queue.append([t,w*weight])
                        visit.add(t)
                
            return -1
        
        
        return [bfs(q[0],q[1]) for q in queries ]
            
