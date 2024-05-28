class Solution:
    def compress(self, chars: List[str]) -> int:
        index = 0
        i = 0

        while i < len(chars) :
            letter = chars[i]
            freq = 1

            while i+1 < len(chars) and letter == chars[i+1] :
                freq += 1
                i += 1

            chars[index] = letter
            index += 1

            if freq > 1 :
                for no in str(freq) :
                    chars[index] = no
                    index += 1

            i += 1

        chars = chars[:index]
        return index