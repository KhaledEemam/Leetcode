class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        students_pref = [0,0]
        for student in students : 
            students_pref[student] += 1
            
        k = 0
        while k < len(sandwiches) :
            if students_pref[sandwiches[k]] > 0 :
                students_pref[sandwiches[k]] -= 1
            else :
                break
            
            k += 1
            
        
        return len(sandwiches)-k