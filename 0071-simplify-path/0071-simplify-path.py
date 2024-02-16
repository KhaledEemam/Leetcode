class Solution:
    def simplifyPath(self, path: str) -> str:
        
        folders = []
        folder = ''
        
        for s in path + '/' :
            if s == '/' :
                if folder =='..' :
                    if folders : folders.pop()
                elif folder != "" and folder != '.' :
                    folders.append(folder)
                folder = ''
            else :
                folder += s
                
                
        return '/'+'/'.join(folders)
                
            