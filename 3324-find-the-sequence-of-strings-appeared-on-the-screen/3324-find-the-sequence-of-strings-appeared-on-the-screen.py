class Solution:
    def stringSequence(self, target: str) -> List[str]:
        alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o",
         "p", "q", "r", "s", "t", "u", "v", "w", "x", 'y', "z"]
        answer = []
        currentString = ""

        def addLetter(word,currentArray) :
            index = len(word)
            targetLetter = target[index]
            letterAlphabeticOrder = ord(targetLetter) - ord("a") + 1

            for i in range(letterAlphabeticOrder) :
                currentArray.append(word + alphabet[i])
            
            word = word + targetLetter

            return word , currentArray

        while len(currentString) < len(target) :

            currentString , answer = addLetter(currentString,answer)


        return answer



