class Solution:
    def myAtoi(self, s: str) -> int:
        s=s.strip()

        if not s:
            return 0
        
        sign=1
        result=0

        if s[0]=='-' or s[0]=='+':
            if s[0]=='-':
                sign=-1
            s=s[1:]

        for char in s:
            if not char.isdigit():
                break
            result=result*10+int(char)  #standard way of constructing the integer from the string's digits. (string->int)

        result=result*sign
        if result< -2 ** 31:
            return -2**31   #returns the lower bound of the 32-bit signed integer range.
        elif result> 2**31-1:
            return 2**31
        
        return result