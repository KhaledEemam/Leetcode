class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        
        counter = {}
        for i in range(len(nums)):
            num = nums[i]
            if num in counter:
                if abs(counter[num] - i) <= k :
                    return True
                else :
                    counter[num] = i
            else :
                counter[num] = i
                
        return False
        