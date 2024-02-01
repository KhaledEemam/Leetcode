class Solution:
    def isPalindrome(self, s: str) -> bool:
        text = ''
        for letter in s :
            if letter.isalpha()  :
                text += (letter.lower())
            elif letter.isdigit() :
                text += letter
                
        l , r = 0 , len(text)-1
        
        
        while l < r :
            if text[l] == text[r] :
                l += 1 
                r -= 1
            else :
                return False
            
        return True
                
            
            
                
        