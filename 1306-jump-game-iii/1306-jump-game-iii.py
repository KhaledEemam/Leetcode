from collections import deque

class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        if arr[start] == 0 : 
            return true
        
        zeroExisted = False
        for num in arr :
            if num == 0 :
                zeroExisted = True
        
        if zeroExisted == False : return False

        queue = deque()
        visited = set()
        queue.append(start)
        visited.add(start)
        
        while queue :

            for _ in range(len(queue)) : 
                index = queue.popleft()

                if arr[index] == 0 : return True

                leftNumber , rightNumber = index - arr[index] , index + arr[index]

                if (leftNumber not in visited) and (leftNumber >= 0) :
                    queue.append(leftNumber)
                    visited.add(leftNumber)

                if (rightNumber not in visited) and (rightNumber < len(arr)) :
                    queue.append(rightNumber)
                    visited.add(rightNumber)

        return False

