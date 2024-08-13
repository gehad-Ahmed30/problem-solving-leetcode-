from typing import List
class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        concate_list=list(zip(names,heights))
        output=sorted(concate_list,result=lambda x:x[1], reverse=True )
        sorted_name=[]
        for names,heights in output:
            sorted_name.append(names)
        return sorted_name


            
