class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        counts = {}
        
        for i in nums :
            if i in counts.keys() :
                counts[i] += 1
            else :
                counts[i] = 1
            
        st_index = 0
        end_index = 0
        
        while len(counts.keys()) > 0:
            element = min(counts.keys())
            count = counts[element]
      
            end_index = end_index + count
            
            for n in range(st_index,end_index,1):
                nums[n] = element
            
            st_index = end_index
            del counts[element]
            
            
        