class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        my_hash = {}
        for i in s :
            if i in my_hash :
                my_hash[i] += 1
            else :
                my_hash[i] = 1
                
        for i in t :
            if i not in my_hash :
                return False
            elif my_hash[i] == 1 :
                del my_hash[i]
            else :
                my_hash[i] -= 1
                
        return True if len(my_hash) == 0 else False
        