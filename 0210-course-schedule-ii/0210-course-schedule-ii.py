class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        courses_pre = {c : [] for c in range(numCourses)}
    
        for pre in prerequisites :
            courses_pre[pre[0]].append(pre[1])


        taken = []

        def dfs(course,cycle) :
            if not courses_pre[course] and course not in taken :
                taken.append(course)
                return 1

            if course in taken :
                return 1

            if course in cycle :
                return 0
            cycle.add(course)

            for preq in courses_pre[course] :
                if dfs(preq,cycle) == 0 :
                    return 0

            taken.append(course)
            return 1

        [dfs(i,set()) for i in range(numCourses)]
        return taken if len(taken) == numCourses else []