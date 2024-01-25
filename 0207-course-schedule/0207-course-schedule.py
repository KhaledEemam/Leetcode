class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        visit = set()
        my_courses = {i : [] for i in range(numCourses)}
        
        for c,p in prerequisites :
            my_courses[c].append(p)
        
        def dfs(course) :
            if course in visit :
                return False
            if my_courses[course] == []:
                return True
            
            visit.add(course)
            for pre in my_courses[course] :
                if dfs(pre) == False : return False
            visit.remove(course)
            my_courses[course] = []
            return True
                
        
        for course in my_courses.keys() :
            if dfs(course) == False : return False
        return True
            
                
            
        
            