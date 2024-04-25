class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        max_count = float("-inf")
        for sentence in sentences :
            sentence_words = sentence.split()
            max_count = max(max_count,len(sentence_words))
            
        return max_count