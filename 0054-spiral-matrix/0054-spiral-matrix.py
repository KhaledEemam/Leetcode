class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        l , r = 0 , len(matrix[0])
        top , bottom = 0 , len(matrix)
        res = []
        
        while r > l and bottom > top :
            
            for i in range(l,r) :
                res.append(matrix[l][i])
                
            top += 1
            
            for i in range(top,bottom) :
                res.append(matrix[i][r-1])
                
            r -= 1
            
            if not(r > l and bottom > top) :
                break
            
            for i in range(r-1,l-1,-1):
                res.append(matrix[bottom-1][i])
            
            bottom -= 1
            
            for i in range(bottom-1,top-1,-1):
                res.append(matrix[i][l])
            
            l += 1
            
            
        return res
                
     
        
            