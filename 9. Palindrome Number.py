class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0:
            return False      #-121  !=   121-
        if x<10:
            return True       # 1 = 1
        
        num=x
        revere_num=0
        while x >0:
            last_digit=x%10    #321 % 10 =1
            revere_num=revere_num*10 + last_digit     #0* 10 + 1=1
            x //=10         #Update the original number by removing the last digit  num=32

        return revere_num==num