class Solution:
    def hIndex(self, citations: List[int]) -> int:
        
        def merge_array(list_1,list_2) :
            l,r = 0 , 0
            final_list = []
            while ((l < len(list_1)) and (r < len(list_2))) :
                if list_1[l] >= list_2[r] :
                    final_list.append(list_1[l])
                    l += 1
                else :
                    final_list.append(list_2[r])
                    r += 1
                    
            if l == len(list_1):
                final_list += list_2[r:]
            elif r == len(list_2) :
                final_list += list_1[l:]
            
            return final_list
                
            
            
        def sort_list(citations) :
            if len(citations) == 1 :
                return citations
            
            l , r = 0 , len(citations)
            
            mid = (l+r) // 2

            list_1 = sort_list(citations[:mid])
            list_2 = sort_list(citations[mid:])
            return merge_array(list_1,list_2)
        
        
        sorted_array = sort_list(citations)
        count = 0
        for i in range(len(sorted_array)):
            if sorted_array[i] >= i+1 :
                count += 1
                
        return count
        
        return count