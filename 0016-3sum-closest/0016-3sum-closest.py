class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        answer = 0
        currentDifference = float('inf') 
        

        for firstNumberIndex , firstNumber in enumerate(nums) :
            left , right = firstNumberIndex + 1 , len(nums) - 1 

            while left < right :
                currentSum = firstNumber + nums[left] + nums[right]
                difference = target - currentSum
                if abs(difference) < currentDifference :
                    currentDifference = abs(difference)
                    answer = currentSum

                if difference > 0 :
                    left += 1
                elif difference < 0 :
                    right -= 1
                else :
                    return target


        return answer