class Solution:
    def trap(self, height: List[int]) -> int:
        
        max_left = 0
        max_left_array = [0] * len(height)

        for  i in range(1,len(height)) :
            max_left = max(max_left,height[i-1])
            max_left_array[i] = max_left


        max_right = 0
        max_right_array = [max_right] * len(height)
        for  i in range(len(height)-2,-1,-1) :
            max_right = max(max_right,height[i+1])
            max_right_array[i] = max_right

        res = 0
        for i in range(len(height)) :
            min_l_r = min(max_left_array[i],max_right_array[i])
            trapped_water = min_l_r - height[i]
            if trapped_water > 0 :
                res += trapped_water


        return res

            
        
        
        
            
            
        