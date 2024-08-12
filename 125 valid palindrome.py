class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=s.lower()
        """for char in s:          #limited Exceeded
            if char.isalpha() or char.isnumeric():
                output.append(char)
            result=''.join(map(str,output))
        return result==result[::-1]"""

        result=''.join(char for char in s if char.isalpha() or char.isnumeric() )
        return result==result[::-1]


        
