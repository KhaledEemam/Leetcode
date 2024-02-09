class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        
        my_hash = {}
        
        for i in range(len(s)) :
            if s[i] in my_hash :
                if my_hash[s[i]] != t[i] :
                    return False
            
            else :
                if t[i] in my_hash.values():
                    return False
                my_hash[s[i]] = t[i]
                
        return True
                
        