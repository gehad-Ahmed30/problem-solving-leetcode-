class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if sorted(s)==sorted(t):              #if string not to convert to list for sort
         return True
        else:
           return False