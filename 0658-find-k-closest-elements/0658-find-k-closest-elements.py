class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        arr.sort()

        left, right = 0 , len(arr) -1 

        while (right - left + 1 ) > k :
            if (abs(arr[left] - x))  <= (abs(arr[right] - x)) :
                right -= 1
            else :
                left +=1
                
        
        return arr[left:right+1]