from typing import List
class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        words=sorted(words,key=len)     #list
        output=[]

        for i in range(len(words)):       #len not +1 beacuse list not ingeter
            for j in range(i+1,len(words)):
                if words[i] in words[j]:
                    output.append(words[i])
                    break
        return output

