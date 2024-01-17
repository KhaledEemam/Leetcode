class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        counts = [0] * 3
        
        for i in nums :
            if i == 0 :
                counts[0] += 1
            elif i == 1 :
                counts[1] += 1
            else :
                counts[2] += 1
            
        st_index = 0
        end_index = 0
        
        for i in range(len(counts)) :
            element = i
            count = counts[i]
            end_index = end_index + count
            
            for n in range(st_index,end_index,1):
                nums[n] = element
            
            st_index = end_index
            
            
        