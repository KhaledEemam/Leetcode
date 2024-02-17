class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        res = []
        start , end = intervals[0][0] , intervals[0][-1]
        
        for interval in intervals :
            if interval[0] <= end :
                
                end = max(interval[-1],end)
            else :
                res.append([start,end])
                start = interval[0]
                end = interval[1]
         
        res.append([start,end])
        return res
                
            
        