from collections import defaultdict
class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        substrings = defaultdict(int)

        if len(s) < 10 : return []

        for i in range(0,len(s)-10+1) : 
            substring = s[i:i+10]
            substrings[substring] += 1

        answer = []
        for key,value in substrings.items() :
            if value > 1 :
                answer.append(key)
        
        return answer
        