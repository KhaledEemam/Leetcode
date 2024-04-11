class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        word1_ = [0] * 26
        word2_ = [0] * 26
        
        for ch in word1 :
            word1_[ord(ch) - ord("a")] += 1
        
        for ch in word2 :
            word2_[ord(ch) - ord("a")] += 1
            
        for index in range(len(word1_)) :
            if (word1_[index] == 0 and word2_[index] != 0) or (word2_[index] == 0 and word1_[index] != 0) :
                return False
            
        word1_.sort()
        word2_.sort()
        
        for i in range(len(word1_)) :
            if word1_[i] != word2_[i] :
                return False
            
        return True
        