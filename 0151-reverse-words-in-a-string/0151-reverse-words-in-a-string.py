class Solution:
    def reverseWords(self, s: str) -> str:
        words = []
        cur_word = ''
        
        for i in range(len(s)) :
            if s[i] != ' ' :
                cur_word += s[i]
            if ((s[i] == ' ') or (i == len(s)-1)) :
                words.append(cur_word)
                cur_word = ''
            
        res = ''
        for i in range(len(words)-1,-1,-1) :
            if words[i] != '' :
                res += words[i] + ' '
                
        return res[:-1]
            
                
            
        
        
        