class Solution:
    def removeStars(self, s: str) -> str:
        letters = []
        
        for letter in s :
            if letter != "*" :
                letters.append(letter)
            else :
                letters.pop()
                
        return "".join(letters)
        