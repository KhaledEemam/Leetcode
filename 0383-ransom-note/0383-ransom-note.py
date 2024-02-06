class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        my_strings = {}
        
        for c in magazine :
            if c in my_strings :
                my_strings[c] += 1
            else :
                 my_strings[c] = 1
                    
                    
        for c in ransomNote :
            if c not in my_strings :
                return False
            elif c in my_strings and my_strings[c] >= 1 :
                my_strings[c] -= 1
                if my_strings[c] == 0 :
                    del my_strings[c]
                    
        return True
                
                
        