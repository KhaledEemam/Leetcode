class TrieNode :
    def __init__(self) :
        self.children = {}
        self.endofword = False
        

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()
        
        for word in words :
            cur = root
            for c in word :
                if c not in cur.children :
                    cur.children[c] = TrieNode()
                cur = cur.children[c]
            cur.endofword = True
                
                
        ROWS , COLUMNS = len(board) , len(board[0])
        visit = set()
        res = set()
        
        def dfs(r, c , node , word) :
            if r < 0 or c < 0 or r == ROWS or c == COLUMNS or board[r][c] not in node.children  or (r,c) in visit :
                return
            
            visit.add((r,c))
            node = node.children[board[r][c]]
            word = word + board[r][c]
            
            if node.endofword :
                res.add(word)
            
            dfs(r + 1, c , node , word)
            dfs(r - 1, c , node , word)
            dfs(r, c + 1, node , word)
            dfs(r, c - 1, node , word)
            visit.remove((r,c))
            
            return
        
        for i in range(ROWS) :
            for j in range(COLUMNS) :
                dfs(i, j , root , "")
                
                
        return list(res)
        
        
            
            
            
            
        