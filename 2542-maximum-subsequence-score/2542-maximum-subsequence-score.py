class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        pairs = [(a,b) for a,b in zip(nums1,nums2)]
        
        pairs = sorted(pairs, reverse = True, key = lambda p : p[1])
        min_heap = []
        res = 0
        cur_sum = 0 
        
        for n1, n2 in pairs :

            heapq.heappush(min_heap,n1)
            cur_sum += n1
            
            if len(min_heap) == k :
                res = max(res ,cur_sum *  n2)
                p = heapq.heappop(min_heap)
                cur_sum -= p
                
        return res
                
            
                
            
            