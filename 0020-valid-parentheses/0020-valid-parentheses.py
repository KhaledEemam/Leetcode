class Solution:
    def isValid(self, s: str) -> bool:
        mystring = []
        
        closeToOpen = {')':'(' , '}' : '{' , ']' : '[' }
        
        for c in s :
            if c in closeToOpen : 
                if mystring and mystring[-1] == closeToOpen[c] :
                    mystring.pop()
                else :
                    return False
            else : 
                mystring.append(c)
                
        return True if not mystring else False