class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        numbers = [i for i in range(1,n+1)]
        res = []
    
        def backtrack(curlist,numbers_list) :
            if len(curlist) == k :
                res.append(curlist)
                return

            for q in range(len(numbers_list)):
                backtrack(curlist + [numbers_list[q]] , numbers_list[q+1:])

        backtrack([],numbers)
        return res
        
                
                
                
            
        