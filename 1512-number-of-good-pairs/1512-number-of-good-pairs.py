class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        numbers_freq_pairs = {}
        
        for num in nums :
            if num not in numbers_freq_pairs :
                numbers_freq_pairs[num] = (1,0) # count , pairs
            else :
                count , pairs_no = numbers_freq_pairs[num]
                pairs_no += count
                count += 1
                numbers_freq_pairs[num] = (count,pairs_no)

        result = 0
        for freq , pairs_no in numbers_freq_pairs.values() :
            if freq > 1 :
                result += pairs_no
            
        return result
        
        
        