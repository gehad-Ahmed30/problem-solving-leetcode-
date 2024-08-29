from typing import List
class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        s=set()
        
        for i in paths:
            s.add(i[0])
            
        
        for i in paths:
            if i[1] not in s:
                return i[1]
        
