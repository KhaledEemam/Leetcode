class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        numbers.sort()
        l , r = 0 , len(numbers) -1
        
        while r > l :
            two_sum = numbers[l] + numbers[r]
            if two_sum > target :
                r -= 1
            elif two_sum < target :
                l += 1
            else :
                return [l+1,r+1]
                
        
        """
        my_hash = {}
        
        for i in range(len(numbers)) :
            diff = target - numbers[i]
            if diff in my_hash :
                return [my_hash[diff]+1,i+1]
            else :
                my_hash[numbers[i]] = i
        """