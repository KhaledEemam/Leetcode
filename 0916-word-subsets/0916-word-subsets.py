from collections import defaultdict

class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        counter = defaultdict(int)

        for word in words2 :
            subCounter = defaultdict(int)
            for letter in word :
                subCounter[letter] += 1
            
            for key,value in subCounter.items() :
                if key not in counter :
                    counter[key] = value
                else :
                    counter[key] = max(value , counter[key])
        
        wordCounter = defaultdict(int)
        answer = []

        for word in words1 :
            universal = True

            for letter in word :
                wordCounter[letter] += 1
            
            for key,value in counter.items() :
                if key not in wordCounter or counter[key] > wordCounter[key] :
                    universal = False
                    break
            

            wordCounter = defaultdict(int)
            if universal :
                answer.append(word)

        return answer
