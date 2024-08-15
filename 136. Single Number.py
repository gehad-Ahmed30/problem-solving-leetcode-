from typing import List
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        for i in nums:
           if nums.count(i) == 1:
               return i
        

# other solution using stack runtime <

from typing import List
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        output=[]
        for i in nums:
            if i not in output:
                output.append(i)
            else:
                output.remove(i)
        return output.pop()