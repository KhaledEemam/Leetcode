class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        len1 , len2 = len(str1) , len(str2)
        def is_devisor(substring) :
            if len(str1) % len(substring) or len(str2) % len(substring) : 
                return False
            
            v1 , v2 = len(str1) // len(substring) , len(str2) // len(substring)
            
            return ((v1 * substring) == str1) and ((v2 * substring) == str2)

        
        for i in range(min(len1,len2) , 0 , -1) :
            if is_devisor(str1[:i]) :
                return str1[:i]
            
        return ''
            
            
                    
                
        