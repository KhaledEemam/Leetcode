class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        left_heap , right_heap = [] , []
        left , right = 0 , len(costs) - 1
        cost = 0
        heapq.heapify(left_heap)
        heapq.heapify(right_heap)
        
        for session in range(k) :
            
            while right >= left and (len(left_heap) < candidates or len(right_heap) < candidates) :
                
                if right >= left and len(left_heap) < candidates :
                    heapq.heappush(left_heap,costs[left])
                    left += 1
                    
                if right >= left and len(right_heap) < candidates :
                    heapq.heappush(right_heap,costs[right])
                    right -= 1
                    
            if left_heap and right_heap :
                left_min =  left_heap[0]
                right_min = right_heap[0]

                if left_min <= right_min :
                    cur_min = heapq.heappop(left_heap)
                    cost += cur_min
                else :
                    cur_min = heapq.heappop(right_heap)
                    cost += cur_min
            elif left_heap :
                cost += heapq.heappop(left_heap)
            else :
                cost += heapq.heappop(right_heap)
                

        return cost
                
                
                    
                    
                
        