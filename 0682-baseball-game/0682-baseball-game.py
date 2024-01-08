class Solution:
    def calPoints(self, operations: List[str]) -> int:
        new_nums = []
        
        for i in operations :
            if i == 'C' :
                new_nums.pop()
            elif i == 'D' :
                double_last_num = new_nums[len(new_nums)-1] * 2
                new_nums.append(double_last_num)
            elif i == '+' :
                n , k = new_nums[len(new_nums)-1] , new_nums[len(new_nums)-2]
                new_nums.append(n+k)
            else :
                new_nums.append(int(i))

            final_sum = 0
            for i in new_nums :
                final_sum += i
            
        return final_sum
                
        
            
                
                
        