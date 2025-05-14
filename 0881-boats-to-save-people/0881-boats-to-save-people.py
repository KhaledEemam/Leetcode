class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        left = 0
        right = len(people) - 1
        boats = 0

        while people[right] == limit and right >= 0:
            boats += 1
            right -= 1
        
        while right >= left :
            
            if right == left : 
                boats += 1
                return  boats
            
            restOfWeight = limit - people[right]

            if restOfWeight < people[left] :
                right -= 1              
            else :
                right -= 1
                left += 1
            
            boats += 1
        
        return boats