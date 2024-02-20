class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        words_count = {}
        for word in words :
            if word in words_count :
                words_count[word] += 1
            else :
                words_count[word] = 1
                
        word_length = len(words[0])
        total_string_length = word_length * len(words)
        res = []
        
        for i in range(len(s)-total_string_length+1) :
            substring = s[i:i+total_string_length]
            words_included = [substring[j:j+word_length] for j in range(0,len(substring),word_length)]
            current_count = {}
            for word in words_included :
                if word in current_count :
                    current_count[word] += 1
                else :
                    current_count[word] = 1
                    
            if current_count == words_count :
                res.append(i)
                
                
        return res
                
            
                
                
        