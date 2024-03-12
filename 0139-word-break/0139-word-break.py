class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        index = 0
        s_length = len(s)
        memo = {}
        
        def get_word(l) :
            if l == s_length :
                return True
            
            if l in memo :
                return False
            
            for word in wordDict :
                word_length = len(word)
                if word == s[l:l+word_length] :
                    if get_word(l+word_length) :
                        return True
                
            memo[l] = False
            return False
        
        
        
        return get_word(0)
            
        