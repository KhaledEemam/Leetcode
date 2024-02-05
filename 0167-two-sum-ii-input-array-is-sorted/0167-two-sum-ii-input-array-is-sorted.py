class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        my_hash = {}
        
        for i in range(len(numbers)) :
            diff = target - numbers[i]
            if diff in my_hash :
                return [my_hash[diff]+1,i+1]
            else :
                my_hash[numbers[i]] = i
        