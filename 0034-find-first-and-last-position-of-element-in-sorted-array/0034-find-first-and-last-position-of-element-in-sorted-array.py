class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        
        
        l , r = 0 , len(nums) - 1 
        
        def get_binary_search(l , r , start) :
            i = -1
            
            while r >= l :
                m = (l + r) // 2
                
                if nums[m] > target :
                    r = m - 1
                    
                if nums[m] < target :
                    l = m + 1
                    
                if nums[m] == target :
                    
                    if start :
                        i = m
                        r = m - 1
                    else :
                        i = m
                        l = m + 1
            return i
        
        s , e = get_binary_search(l , r , True) , get_binary_search(l , r , False)
        return [s,e]