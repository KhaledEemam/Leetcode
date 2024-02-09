class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        hash_1 , hash_2 = {} , {}
        s_list = s.split(' ')
        
        for l , r in zip(pattern,s_list ) :
            if (l in hash_1 and hash_1[l] != r) or (r in hash_2 and hash_2[r] != l)  :
                return False
            
            hash_1[l] = r
            hash_2[r] = l
                
        return True if len(s_list) == len(pattern) else False
            
            
        