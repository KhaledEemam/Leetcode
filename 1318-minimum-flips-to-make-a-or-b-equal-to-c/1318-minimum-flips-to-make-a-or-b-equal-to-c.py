class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        changes = 0
        
        while a != 0 or b!= 0 or c!= 0  :
            bit_a = a & 1
            bit_b = b & 1
            bit_c = c & 1
            a = a >> 1
            b = b >> 1
            c = c >> 1
            
            if bit_c == 1 :
                if (bit_a | bit_b ) != 1 :
                    changes += 1
            else :
                if bit_a != 0 :
                    changes += 1

                if bit_b != 0 :
                    changes += 1
                    
                    
        return changes
        