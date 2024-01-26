class Solution:
    def rob(self, nums: List[int]) -> int:
        one , two = 0 , 0
        
        # [one,two,n,n+1,n+2, ....]
        for num in nums :
            temp = max(one+num , two)
            one = two
            two = temp
        return temp
            
        