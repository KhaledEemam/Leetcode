class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        answer = []

        if numRows > 0 :
            answer.append([1])


        for rowIndex in range(1,numRows) :
            current_row = [1] * (rowIndex+1)

            for i in range(1,len(current_row)-1) :
                current_row[i] = answer[-1][i-1] + answer[-1][i]

            answer.append(current_row)
 
        return answer        