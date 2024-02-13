class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def back_track(l,r,cur_string) :
            if l == r and len(cur_string) == 2*n :
                res.append(cur_string)
                return

            if l < n :
                back_track(l+1,r,cur_string+"(")

            if l > r  :
                back_track(l,r+1,cur_string+")")


        back_track(0,0,'')
        return res