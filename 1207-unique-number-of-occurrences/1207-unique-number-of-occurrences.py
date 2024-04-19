class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        arr = sorted(arr)
        count = 1
        number = arr[0]
        occurences = set()
        
        for i in range(1,len(arr)) :
            if arr[i] != arr[i-1] :
                
                if count in occurences :
                    return False
                else :
                    occurences.add(count)
                    
                count = 0
                number = arr[i]
            
            count += 1
            
        return False if count in occurences else True
                