import math
import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        def get_distance (corrdinates) :
            distance = math.sqrt(corrdinates[0]**2 + corrdinates[1]**2 )
            return distance
        
        distances = []
        res = []
        
        for point in points :
            distance = get_distance(point)
            distances.append([distance,point[0],point[1]])
            
                
        heapq.heapify(distances)
        n = 0
        
        while n < k and len(distances) > 0 :
            point = heapq.heappop(distances)
            res.append([point[1],point[2]])
            n += 1
            
                    
            
        return res     