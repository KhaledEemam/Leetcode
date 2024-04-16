class Solution:
    def decodeString(self, s: str) -> str:
        res = ""
    
        def dfs(index,res) :
            while index < len(s) :
                if s[index] == "]" :
                    return index , res

                elif s[index].isdigit() :
                    l = index
                    while s[index].isdigit() :
                        index = index + 1

                    times = int(s[l:index])
                    index = index + 1
                    index , cur_string = dfs(index,"")
                    res += times * cur_string

                else :
                    res += s[index]

                index += 1

            return index , res

        _ , res = dfs(0,res)

        return res