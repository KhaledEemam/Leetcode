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

        
        """
        word1 = "".join(sorted(word1))
        word2 = "".join(sorted(word2))
        
        if word1 == word2 :
            return True
        
        word1_dict = defaultdict(int)
        word2_dict = defaultdict(int)
        
        for letter in word1 :
            word1_dict[letter] += 1
            
        for letter in word2 :
            word2_dict[letter] += 1
            
        if set(word1_dict.keys()) != set (word2_dict.keys()) :
            return False
        else :     
            if sorted(list(word1_dict.values())) == sorted(list(word2_dict.values())) :
                return True
            else :
                return False
            
        
        """    


        