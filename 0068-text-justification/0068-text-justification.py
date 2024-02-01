class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        line , length = [] , 0
        res = []
        
        i = 0 
        while i < len(words) :
            if (length + len(line) + len(words[i]) > maxWidth) :
                
                spaces = (maxWidth - length) // (max(1,len(line)-1))
                remainder = (maxWidth - length) % (max(1,len(line)-1))
                
                for j in range(max(1,len(line)-1)) :
                    line[j] += ' '*spaces
                    if remainder :
                        line[j] += ' '
                        remainder -= 1
                        
                res.append(''.join(line))
                length , line = 0 , []
                        
            
            line.append(words[i])
            length += len(words[i])
            i += 1
            
        
        last_line = ' '.join(line)
            
        right_spaces = maxWidth - len(last_line)
        last_line += ' '*right_spaces
        res.append(last_line)
        return res
            
            
        