class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        
        if len(haystack) > len(needle) :
            for i in range(len(haystack)-len(needle)+1) :
                if haystack[i:i+len(needle)] == needle :
                    return i
        elif len(haystack) == len(needle) :
            if haystack == needle :
                return 0

        return -1
                    
                    
        