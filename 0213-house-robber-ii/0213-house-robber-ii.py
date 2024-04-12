class Solution:
    def rob(self, nums: List[int]) -> int:
        
        def get_max_rob(my_nums):
            one , two = 0 , 0
            
            for num in my_nums :
                temp = max(one+num,two)
                one = two
                two = temp
                
            return two
        
        if len(nums) == 1 : return nums[0] 
        
        n1 = get_max_rob(nums[:-1])
        n2 = get_max_rob(nums[1:])
        
        return max(n1,n2)
        