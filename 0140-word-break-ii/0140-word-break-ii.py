class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        memo = {}
        answer = []
        
        def get_sentences(current_sentence, current_word , index) :
            if index == len(s) and current_word == '' :
                answer.append(current_sentence)
                return
            
            if index == len(s) :
                return
            
            current_word = current_word + s[index]

            if current_word in wordDict :
                if len(current_sentence) > 0 :
                    get_sentences(current_sentence + " " + current_word , '' , index+1)
                else :
                    get_sentences( current_word , '' , index+1)

            
            get_sentences(current_sentence , current_word , index+1)


        
        get_sentences("","",0)
        return answer