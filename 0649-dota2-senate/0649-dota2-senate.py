class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        R , D = deque() , deque()
        
        for i , s in enumerate(senate) :
            if s == "R" :
                R.append(i)
            else :
                D.append(i)
                
        
        while R and D :
            rturn = R.popleft()
            dturn = D.popleft()
            
            if rturn < dturn :
                R.append(rturn+len(senate))
            else :
                D.append(dturn+len(senate))
                
            
            
        return "Dire" if not R else "Radiant"
        