class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l , r = 0 ,0
        max_res = 0
        strings = set()
        
        
        while r < len(s) :
            
            while  r < len(s) and s[r] not in strings :
                strings.add(s[r])
                r += 1
                
            if r == len(s) :
                max_res = max(max_res,r-l)
                
             
            while r < len(s) and s[r] in strings: 
                max_res = max(max_res,r-l)
                strings.remove(s[l])
                l += 1
            
            
        return max_res
            
            
        