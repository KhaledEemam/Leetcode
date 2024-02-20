class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        
        points.sort()
        count = 1
        
        left = points[0][0]
        right = points[0][1]
        
        for i in range(1,len(points)) :
            if points[i][0] <= right :
                left = max(left,points[i][0])
                right = min(right,points[i][1])
            else :
                left =points[i][0]
                right = points[i][1]
                count += 1
                
        return count
             
            
        