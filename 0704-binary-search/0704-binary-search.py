class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        low , high = 0 , len(nums)-1
        
        mid = (low + high) // 2
        
        while high >= low :
            if nums[mid] > target :
                high = mid -1
                mid = (low + high) // 2
            elif nums[mid] < target :
                low = mid +1 
                mid = (low + high) // 2
            else :
                return mid
            
        return -1