class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        def get_perm(curlist) :
            if len(curlist) == len(nums) :
                res.append(curlist)
                return
            
            for num in nums :
                if num not in curlist :
                    get_perm(curlist+[num])
                
                
        
        
    
        
        get_perm([])
        return res
                
                
        