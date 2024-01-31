class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(cost) > sum(gas) :
            return -1
        
        start = 0
        total = 0
        
        for i in range(len(gas)-1) :
            total += gas[i] - cost[i]
            if total < 0 :
                total = 0
                start = i+1
                
        return start
        """ 
        def check(i) :
            cur_station = i
            gas_amount = gas[i]
            cost_to_next = cost[i]

            while cost_to_next <= gas_amount :

                i += 1
                if i == len(gas) :
                    i = 0
                if i == cur_station :
                    return i

                gas_amount =  gas_amount - cost_to_next + gas[i]
                cost_to_next = cost[i]

            return -1
       
        for i in range(len(gas)) :
            if cost[i] > gas[i] :
                pass
            else :
                output = check(i)
                if output != -1 :
                    return output

        return -1
        """

        
        
        