class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = []
        
        for i in s :
             if i.lower() in ('a' , 'e' , 'i' , 'o' , 'u') :
                    vowels.append(i)
                    
        res = ''
        for i in s :
            if i.lower() in ('a' , 'e' , 'i' , 'o' , 'u') :
                    res  += vowels.pop()
            else :
                res += i
                
        return res
        