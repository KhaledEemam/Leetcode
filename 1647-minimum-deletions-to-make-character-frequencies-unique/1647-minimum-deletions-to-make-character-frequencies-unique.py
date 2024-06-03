class Solution:
    def minDeletions(self, s: str) -> int:
        numbers_set = set()
        deletions = 0
        s = ''.join(sorted(s))
        char = ''
        freq = 0

        for i in range(len(s)) :
            if i+1 >= len(s) or s[i] != s[i+1] :
                freq += 1
                while freq in numbers_set and freq > 0 :
                    deletions += 1
                    freq -= 1

                numbers_set.add(freq)
                freq = 0
            
            else :
                freq += 1

        return deletions