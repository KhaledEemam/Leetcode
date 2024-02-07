class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        my_hash = {'2' : ['a','b','c'],
                  '3' : ['d','e','f'],
                  '4' : ['g','h','i'],
                  '5' : ['j','k','l'],
                  '6' : ['m','n','o'],
                  '7' : ['p','q','r','s'],
                  '8' : ['t','u','v'],
                  '9' : ['w','x','y','z']}
        res = []
        
        def get_comp(i,my_string) :
            if len(my_string) == len(digits) :
                res.append(my_string)
                return
            
            for letter in my_hash[digits[i]] :
                get_comp(i+1,my_string + letter)
                
                
            return res
        
        if digits != '' :
            return get_comp(0,'')
        
        return []
        
                
                
            
                
                
            