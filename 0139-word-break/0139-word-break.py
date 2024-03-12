class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        """
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
           """
        dp = [False] * (len(s) + 1)
        dp[-1] = True
        
        for i in range(len(s)-1,-1,-1) :
            for w in wordDict :
                if ((i+len(w)) <= len(s)) and s[i:i+len(w)] == w :
                    dp[i] = dp[i+len(w)]
                    
                if dp[i] == True :
                    break
                    
        return dp[0]
        