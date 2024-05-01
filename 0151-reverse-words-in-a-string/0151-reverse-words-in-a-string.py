class Solution:
    def reverseWords(self, s: str) -> str:
        
        cur_word = ''
        words = []
        for i in range(len(s)) :
            if s[i] != ' ' :
                cur_word = cur_word + s[i]
                
            if s[i] == ' ' or i == len(s)-1 :
                if len(cur_word) > 0 : words.append(cur_word)
                cur_word = ''
            
        print(words)
        res = words[-1]

        for i in range(len(words)-2,-1,-1) :
            res = res + ' ' + words[i]

        return res