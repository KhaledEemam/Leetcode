class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:

        if len(stones) == 1 :
            return stones[0]
        
        
        new_list = stones.copy()
        executed = False
        new_list = [-x for x in new_list]
        
        while len(new_list) >= 2 :
            
            executed = True
            
            heapq.heapify(new_list)
            element_1 = heapq.heappop(new_list)
            element_2 = heapq.heappop(new_list)
            
            if element_1 == element_2 :
                pass
            elif - element_1 > -element_2 :
                new_element = -(-element_1 - -element_2)
                heapq.heappush(new_list,new_element)
            else : 
                new_element = -(-element_2 - -element_1)
                heapq.heappush(new_list,new_element)
                
            
        if len(new_list) == 0 :
            return 0
        else :
            return -new_list[0]
        
            
        