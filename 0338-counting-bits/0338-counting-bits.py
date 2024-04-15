class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = [0] * (n+1)
        
        def get_count(number) :
            count = 0 
            while number :
                if number & 1 == 1:
                    count += 1
                number = number >> 1
                
            return count
        
        for i in range(n+1) :
            ans[i] = get_count(i)
            
        return ans
        
        