class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        numbers = [1 , 2 , 3 , 4 , 5 , 6 , 7 , 8 , 9]
        result = []
        
        def dfs(combination,combination_sum , combination_length ,number_index) :
            if combination_length == k and combination_sum == n :
                result.append(combination)
                return
            
            if combination_length > k and combination_sum > n or number_index >= 9 :
                return
            
            for index in range(number_index,9) :
                dfs(combination + [numbers[index]] ,combination_sum + numbers[index] , combination_length + 1 , index+1)
                
                
        
        dfs([],0,0,0)
        return result