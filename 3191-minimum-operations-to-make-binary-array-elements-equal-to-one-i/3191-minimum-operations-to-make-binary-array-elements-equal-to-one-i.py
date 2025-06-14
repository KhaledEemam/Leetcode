class Solution:
    def minOperations(self, nums: List[int]) -> int:
        answer = 0

        for index in range(len(nums) - 2 ) :

            if index == (len(nums) - 3) :

                lastSum = nums[index] + nums[index + 1] + nums[index + 2]

                if lastSum == 1 or lastSum == 2 :
                    return -1
                elif lastSum == 0 :
                    answer += 1
                    break
                else :
                    break 


            if nums[index] == 1 :
                continue

            answer += 1

            nums[index + 1] = nums[index + 1] ^ 1
            nums[index + 2] = nums[index + 2] ^ 1


        return answer
            
