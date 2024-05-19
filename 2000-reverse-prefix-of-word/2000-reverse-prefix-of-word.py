class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        stack = []
        is_ch_exist = False
        for letter in word :
            stack.append(letter)
            if letter == ch :
                is_ch_exist = True
                break
        
        if is_ch_exist :
            ch_index = len(stack)
            res = ''
            while stack :
                res += stack.pop()


            if ch_index <= len(word) -1 :
                res = res + word[ch_index:]

        return word if not is_ch_exist else res       
                