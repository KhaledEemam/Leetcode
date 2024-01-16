class Solution:
    def mergeArray(self,arr_1:List[int],arr_2:List[int]) -> List[int] :
        i = 0
        total_length = len(arr_1) + len(arr_2)

        sorted_Arr = []


        n , k = 0, 0

        while i < total_length :
            if n == len(arr_1) :
                sorted_Arr += arr_2[k:]
                break
            elif k == len(arr_2) :
                sorted_Arr += arr_1[n:]
                break


            if arr_1[n] < arr_2[k] :
                sorted_Arr.append(arr_1[n])
                i = i + 1
                n = n + 1
            elif arr_1[n] > arr_2[k] :
                sorted_Arr.append(arr_2[k])
                i = i + 1
                k = k + 1
            else : 
                sorted_Arr.append(arr_1[n])
                sorted_Arr.append(arr_2[k])
                n += 1
                k += 1
                i += 2

        return sorted_Arr
        
        
    def sortArray(self, nums: List[int]) -> List[int]:
        st_index = 0
        end_index = len(nums) -1
        
        if ((end_index-st_index) +1 ) <= 1 :
            return nums
        
        m = ( end_index - st_index ) // 2
        
        arr_1 = self.sortArray(nums[st_index:m+1])
        arr_2 = self.sortArray(nums[m+1:end_index+1])
        
        return self.mergeArray(arr_1,arr_2)
        
        
        