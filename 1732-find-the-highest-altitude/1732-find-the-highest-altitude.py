class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        max_alt , cur_alt = 0 , 0
        
        for num in gain :
            cur_alt += num
            max_alt = max(max_alt,cur_alt)
            
        return max_alt
        