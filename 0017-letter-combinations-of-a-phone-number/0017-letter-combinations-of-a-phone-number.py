class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0 : return []
        num_chars = {"2":"abc" , "3":"def", "4":"ghi","5":"jkl","6":"mno","7":"pqrs",
                    "8":"tuv","9":"wxyz"}
        ans_len = len(digits)
        ans = []
        
        def dfs(index,cur_str) :
            if index == ans_len :
                ans.append(cur_str)
                return
            
            for char in num_chars[digits[index]] :
                dfs(index+1,cur_str+char)
                
            return
        
        
        dfs(0,'')
        return ans
            
                
        