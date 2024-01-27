class Solution:
    def countBits(self, n: int) -> List[int]:
        
        def get_count(n) :
            count = 0 
            
            while n > 0 :
                if n & 1 == 1:
                    count += 1
                n = n>>1
                
            return count
        
        my_array = [0] * (n+1)
        
        for i in range(n+1) :
            count = get_count(i)
            my_array[i] = count
            
        return my_array
        
        
        