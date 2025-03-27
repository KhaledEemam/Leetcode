class Solution:
    def divisibilityArray(self, word: str, m: int) -> List[int]:
        remainder = 0
        div = [0] * len(word)

        for i in range(len(word)) :
            digit = ord(word[i]) - ord("0")
            remainder = ((remainder * 10 ) + digit) % m

            if remainder == 0 :
                div[i] = 1
        
        return div