class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        lis = [1] * len(nums)
        
        for i in range(len(nums)-1,-1,-1) :
            for j in range(i,len(nums)) :
                if nums[j] > nums[i] :
                    lis[i] = max(lis[i],1+lis[j])

                    
        return max(lis)