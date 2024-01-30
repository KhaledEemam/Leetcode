class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        my_hash = {}
        
        for num in nums :
            if num not in my_hash :
                my_hash[num] = 1
            else :
                 my_hash[num] += 1
       
        max_count = 0
        for num , count in my_hash.items() :
            if count > max_count :
                max_count = count
                number = num
                
        return number
            
            
                
                
            