class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        l , r = 0 , 0
        result = ''
        
        while l < len(word1) and r < len(word2) :
            
            result += word1[l] + word2[r]
            l += 1
            r += 1
            
            
        if l == len(word1) :
            result += word2[r:]
            
        if r == len(word2) :
            result += word1[l:]
            
        return result

            
        