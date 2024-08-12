class Solution:
    def sortSentence(self, s: str) -> str:
        result=[]
        output=s.split()
        output.sort(key=lambda x: int(x[-1]))
        for x in output:
            result.append(x[:-1])  

        return ' '.join(result)

