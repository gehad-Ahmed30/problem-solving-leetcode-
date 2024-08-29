from typing import List
class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        x=''.join(word1)
        y=''.join(word2)
        return x==y
