from typing import List
class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        for row in matrix:
            print(row)
        result=list(map(list,zip(*matrix)))     #zip(*m) transposes the matrix by unpacking m and grouping elements by their corresponding positions.   
        for row in result:
            print(row)

        return result