# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        
        l = 1
        r = n
        
        while r >= l :
            m = (l+r) // 2
            if isBadVersion(m) == False :
                if isBadVersion(m+1) == True :
                    return m + 1
                l = m
            elif isBadVersion(m) == True :
                if isBadVersion(m-1) == False :
                    return m
                r = m - 1

                
                    
        
        