class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        hash_1 , hash_2 = {} , {}
        
        for l ,r in zip(s,t) :
            
            if ((l in hash_1) and (hash_1[l] != r)) or ((r in hash_2) and (hash_2[r] != l)) :
                return False
            
            
            hash_1[l] = r
            hash_2[r] = l
            
        return True
        