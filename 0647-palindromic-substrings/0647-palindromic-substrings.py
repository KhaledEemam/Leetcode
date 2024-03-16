class Solution:
    def countSubstrings(self, s: str) -> int:
        def get_res(l,r,res) :
            while l >= 0 and r < len(s) and s[l] == s[r] :
                    res += 1
                    l -= 1
                    r += 1
            return res
        
        res = 0 
        
        for i in range(len(s)) :
            l = r = i
            res = get_res(l,r,res)
                
            
            l = i 
            r = i + 1
            res = get_res(l,r,res)
                
        return res
    
        
        
            