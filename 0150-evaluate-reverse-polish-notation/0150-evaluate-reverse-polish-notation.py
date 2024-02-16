import math

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        numbers = []
        def convert_to_operator(char):
            operator_mapping = {
                '+': lambda x, y: x + y,
                '-': lambda x, y: x - y,
                '*': lambda x, y: x * y,
                '/': lambda x, y: math.trunc(x / y),
            }
            return operator_mapping.get(char)

        for token in tokens :

            
            if token.lstrip('-').isdigit():
                numbers.append(int(token))
            else :
                num_2 = numbers.pop()
                num_1 = numbers.pop()
                operator = convert_to_operator(token)
                res = operator(num_1,num_2)
                numbers.append(res)
                
        return numbers[0] if len(tokens) > 0 else None
        