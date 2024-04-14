class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        diff = {}
        pairs = 0
        
        for i in range(len(nums)) :
            if nums[i] in diff :
                pairs += 1
                if diff[nums[i]] > 1 :
                    diff[nums[i]] -= 1
                else :
                    del diff[nums[i]]
                
            else :
                key = k-nums[i]
                if key in diff :
                    diff[key] += 1
                else :
                    diff[key] = 1
                
        return pairs
                
        
        