class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        res = []
        subset = []
        
        def get_subsets(i) :
            if i >= len(nums) :
                res.append(subset.copy())
                return 
            
            subset.append(nums[i])
            get_subsets(i+1)
            
            subset.pop()
            get_subsets(i+1)
            
        get_subsets(0)
        return res
        