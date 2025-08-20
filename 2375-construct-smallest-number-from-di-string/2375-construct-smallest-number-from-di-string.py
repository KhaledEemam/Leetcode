class Solution:
    def smallestNumber(self, pattern: str) -> str:
        answer = [0] * (len(pattern) +1 )
        for i in range(len(answer)-1 ,0,-1) :
            if pattern[i-1] == 'D' :
                answer[i] = -1
                if i+1 < len(answer) :
                    answer[i] = answer[i+1] - 1

        
        currentMax = 1

        for i in range(len(answer)) :
            if answer[i] == 0 :
                answer[i] = currentMax
                currentMax += 1
                if i+1 < len(answer) and answer[i+1] < 0 :
                    answer[i] = answer[i] + (-1 * answer[i+1])
                    currentMax = answer[i] + 1  

            else :
                answer[i] =  answer[i-1] - 1
        
        result = "".join(map(str, answer))
        return result