class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == '' : return ''
        count_t , window = {} , {}
        res , res_count = [-1,-1] , float("inf")
        l  = 0 
       
        
        for letter in t :
            count_t[letter] = 1 + count_t.get(letter,0)
            
        have , need = 0 , len(count_t)
            
        for r in range(len(s)) :
            
            window[s[r]] = 1 + window.get(s[r],0)
            
            
            if s[r] in count_t and window[s[r]] == count_t[s[r]] :
                have += 1
                
            while have == need :
                cur_res = r-l+1
                if cur_res < res_count :
                    res_count = cur_res
                    res = [l,r]
                
                window[s[l]] -= 1
                if s[l] in count_t and  count_t[s[l]] >  window[s[l]] :
                    have -= 1
                
                l += 1
        
        l , r = res
        return s[l:r+1] if res_count != float("inf") else ""
                
            
        