class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words=s.split()
        if len(pattern) !=len(words):
            return False
        """
        pattern = "abba
        s = "dog cat cat dog"
        c (which is 'a') is not in charToWord, so add charToWord['a'] = 'dog'.
        w (which is 'dog') is not in wordToChar, so add wordToChar['dog'] = 'a
        charToWord = {'a': 'dog'}
        wordToChar = {'dog': 'a'}
        """
        charToWorl={}
        worldToChar={}
        """
        zip function in Python is used to iterate over multiple iterables (like lists or tuples)
        """

        for c,w in zip(pattern,words):
            if c in charToWorl and charToWorl[c] != w:
                return False
            if w in worldToChar and worldToChar[w] != c:
                return False
            charToWorl[c]=w
            worldToChar[w]=c
        return True