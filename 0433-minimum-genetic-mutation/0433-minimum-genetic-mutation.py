class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        
        if endGene not in bank :
            return -1
        
        bank.append(startGene)
        nei = collections.defaultdict(list)
        
        for gen_a in bank :
            for gen_b in bank :
                if gen_b == gen_a : continue
                    
                n = 0
                for i in range(len(gen_a)) :
                    if gen_a[i] != gen_b[i] : n += 1
                
                if n == 1 : nei[gen_a].append(gen_b)
                    
        
        visit = set([startGene])
        queue = deque()
        queue.append(startGene)
        steps = 0
        
        while queue : 
            
            for i in range(len(queue)) :
                gene = queue.popleft()
                if gene == endGene :
                    return steps
                
                for g in nei[gene] :
                    if g not in visit :
                        visit.add(g)
                        queue.append(g)
                        
            steps += 1
            
        return -1
        