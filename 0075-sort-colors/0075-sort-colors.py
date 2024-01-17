class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l , r = 0 , len(nums) -1
        i = 0
        def swap(n,k) :
            temp = nums[n]
            nums[n] = nums[k]
            nums[k] = temp
            
        
        while i <= r :
            if nums[i] == 0 :
                swap(l,i)
                l += 1
            elif nums[i] == 2 :
                swap(r,i)
                r -= 1
                i -= 1
            i =i+1
        
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
           """ 
            
        