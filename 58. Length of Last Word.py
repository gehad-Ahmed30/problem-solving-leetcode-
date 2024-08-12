class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        output=s.split()
        x=len(output[-1])
        return x
        