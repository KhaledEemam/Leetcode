from collections import defaultdict
class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        nums.sort()
        products = defaultdict(int)

        for index in range(len(nums)) :
            for secondIndex in range(index+1 , len(nums)) :
                product = nums[index] * nums[secondIndex]
                products[product] += 1

        
        answer = 0 

        for value in products.values() :
            pairs = 0
            for pairCount in range(1,value) :
                pairs += pairCount

            answer += (pairs * 8 ) 

        print(products)
        return answer 

        