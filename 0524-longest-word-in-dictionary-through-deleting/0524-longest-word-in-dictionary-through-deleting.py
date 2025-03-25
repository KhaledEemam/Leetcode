class Solution:
    def findLongestWord(self, s: str, dictionary: List[str]) -> str:
        dictionary.sort()
        longestString, letterCount = "" , 0
        
        def canGet(target) :
            sIndex = len(s) - 1
            targetIndex = len(target) - 1

            while targetIndex >= 0 and sIndex >= 0 :

                if s[sIndex] != target[targetIndex] :
                    sIndex -= 1
                else :

                    if targetIndex == 0 :
                        return True
                    else :
                        sIndex -= 1
                        targetIndex -= 1

            return False

        for word in dictionary :
            wordLength = len(word)
            status = canGet(word)

            if status and wordLength > letterCount :
                letterCount = wordLength
                longestString = word

        return longestString

        