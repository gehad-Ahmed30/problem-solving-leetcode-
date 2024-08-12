from typing import List
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        left,rigth=0, len(s)-1

        while left<rigth:
            s[left],s[rigth]=s[rigth],s[left]
            left+=1
            rigth-=1
