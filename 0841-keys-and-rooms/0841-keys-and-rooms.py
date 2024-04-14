class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        
        visited = set()
        queue = deque()
        queue.append(rooms[0])
        visited.add(0)
        
        while queue :
            
            for i in range(len(queue)) :
                keys = queue.popleft()
                for key in keys :
                    if key not in visited :
                        visited.add(key)
                        queue.append(rooms[key])
        
        for i in range(len(rooms)) :
            if i not in visited :
                return False
            
        return True
                        
        
            
        
        