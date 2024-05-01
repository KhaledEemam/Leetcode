class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowles = 'a', 'e', 'i', 'o','u'
        vowels = set(vowles)
        vowels_no , cur_vowels = 0 , 0
        l , r = 0 , 0
        
        while r < len(s) :
            if s[r] in vowels :
                cur_vowels += 1
            
            if r - l + 1 == k :
                vowels_no = max(vowels_no,cur_vowels)
                if s[l] in vowels :
                    cur_vowels -= 1
                l += 1
            
            r += 1
            
        return vowels_no
            
            
                
            
        