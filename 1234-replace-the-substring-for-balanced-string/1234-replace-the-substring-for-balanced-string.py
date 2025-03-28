from collections import defaultdict
class Solution:
    def balancedString(self, s: str) -> int:
        min_len = float("inf")
        counter = defaultdict(int)

        for letter in s :
            counter[letter] += 1

        balance_value = len(s) // 4
        balanced = True

        for value in counter.values() :
            if value != balance_value :
                balanced = False
        
        if balanced :
            return 0
        
        left = 0
        for right in range(len(s)) :
            counter[s[right]] -= 1

            while all(counter[letter] <= balance_value for letter in "QWER" ) :
                min_len = min(min_len ,( right - left + 1))
                counter[s[left]] += 1
                left += 1

        return min_len