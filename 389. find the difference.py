class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        # not split of string -> ['abcd']
        sum_s=sum(ord(c) for c in s)
        sum_t=sum(ord(c) for c in t)
        return chr(sum_s-sum_t)      #65 -> A
