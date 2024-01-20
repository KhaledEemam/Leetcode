class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        res = []
        subset = []
        
        def get_subsets(i):
            if sum(subset.copy()) > target or i >= len(candidates):
                return
            if sum(subset.copy()) == target :
                res.append(subset.copy())
                return

            
            subset.append(candidates[i])
            get_subsets(i)
            
            subset.pop()
            get_subsets(i+1)
            
        
        get_subsets(0)
        return res