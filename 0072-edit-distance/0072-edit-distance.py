class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        cache = [[float('inf')] *( len(word1)+1)  for j in range(len(word2)+1)]
        
        for i in range(len(cache)) :
            cache[i][len(cache[0])-1] = len(cache) - i -1
            
        for j in range(len(cache[0])) :
            cache[len(cache)-1][j] = len(cache[0]) - j -1 
            
        
        for row in range(len(cache)-2,-1,-1) :
            for column in range(len(cache[0])-2,-1,-1) :
                if word1[column] == word2[row] :
                    cache[row][column] = cache[row+1][column+1]
                else :
                    cache[row][column] = 1 + min(cache[row+1][column] , cache[row][column+1] , cache[row+1][column+1])
                    
        
        return cache[0][0]