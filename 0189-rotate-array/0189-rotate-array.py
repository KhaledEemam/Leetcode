class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        old_nums = nums.copy()
        if k > len(nums) :
            k = k % len(nums)
        for old_index in range(len(nums)) :
            new_index = old_index + k
            if new_index >= len(nums) :
                new_index = new_index - len(nums)

            nums[new_index] = old_nums[old_index]
        """
        n = 0 
        while n < k :
            last_element = nums[len(nums)-1]
            for i in range(len(nums)-1,-1,-1) :
                if ((i-1) < 0 ):
                    nums[0] = last_element
                else :
                    nums[i] = nums[i-1]
            n += 1
        """