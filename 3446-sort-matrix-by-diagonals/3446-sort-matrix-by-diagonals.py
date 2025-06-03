class Solution:
    def sortMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        rows , columns = len(grid) , len(grid[0])

        m = columns - 1
        while m > 0 :
            diagonal = []

            row , column = 0 , m

            while row < rows and column < columns :
                diagonal.append(grid[row][column])
                row += 1
                column += 1

            diagonal.sort()
            row , column = 0 , m

            for value in diagonal :
                grid[row][column] = value
                row += 1
                column += 1

            m -= 1

        n = 0

        while n < rows :
            diagonal = []

            row , column = n , 0

            while row < rows and column < columns :
                diagonal.append(grid[row][column])
                row += 1
                column += 1
            
            diagonal.sort(reverse=True)
            row , column = n , 0

            for value in diagonal :
                grid[row][column] = value
                row += 1
                column += 1

            n += 1
        
        return grid


            

        