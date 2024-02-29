class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList : return 0
        
        wordList.append(beginWord)
        nei = collections.defaultdict(list)
        for word in wordList :
            for j in range(len(word)) :
                key = word[:j] + '*' + word[j+1:]
                nei[key].append(word)
        
        
        queue = deque()
        visit = set([beginWord])
        queue.append(beginWord)
        steps = 1
        
        while queue :
            
            for i in range(len(queue)) :
                word = queue.popleft()
                if word == endWord :
                    return steps
                
                for k in range(len(word)) :
                    key = word[:k] + "*" + word[k+1:]
                    for v in nei[key] :
                        if v not in visit :
                            visit.add(v)
                            queue.append(v)
                            
            steps += 1
                
        return 0