class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def binary_search(nums) :
            left , right = 0 , len(nums) - 1
            mid = (left+right) // 2

            while right >= mid  and right >= left:
                if nums[mid] > target :
                    right = mid - 1
                    mid = (left+right) // 2
                elif nums[mid] < target :
                    left = mid + 1
                    mid = (left+right) // 2
                else :
                    return True
            return False
        
        def check_on_matrix(matrix) :
            last_column = [row[-1] for row in matrix]
            l , r  = 0 , len(last_column) - 1
            m = (l+r) // 2

            while l != m and r != m :
                if last_column[m] > target :
                    r = m
                    m = (l+r)//2
                elif last_column[m] < target :
                    l = m
                    m = (l+r)//2
                else :
                    return m

            if target <= last_column[l] :
                return l
            else : 
                return r
               
        index = check_on_matrix(matrix)
        return binary_search(matrix[index])
        
     