class Solution:
    def calculate(self, s: str) -> int:
        output , cur , sign , stack = 0 , 0 , 1 , []
        
        for c in s :
            if c.isdigit() :
                cur = 10*cur +int(c)
            elif c in "+-" :
                output += (sign * cur)
                if c == '+':
                    sign = 1 
                else :
                    sign = -1
                cur = 0
            elif c == "(" :
                stack.append(output)
                stack.append(sign)
                output = 0
                sign = 1
            elif c ==")" :
                output += (cur * sign)
                output *= stack.pop()
                output += stack.pop()
                cur = 0
                sign = 1
        return output + (cur*sign)