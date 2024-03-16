class Solution:
    def longestPalindrome(self, s: str) -> str:        
        def update_substring(l,r,substring,substring_len) :
            while l >= 0 and r < len(s) and s[l] == s[r] :
                l -= 1
                r += 1
            
            if substring_len < (r-l-1) :
                substring = s[l+1:r]
                substring_len = len(substring)
            
            return substring , substring_len
                
        
        substring_len = 0
        substring = ''    
        
        for i in range(len(s)) :
            l = r = i
            substring , substring_len = update_substring(l,r,substring,substring_len)
                
            l , r = i , i+1
            substring , substring_len = update_substring(l,r,substring,substring_len)
                
        return substring