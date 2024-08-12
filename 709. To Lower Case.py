class Solution:
    def capitalizeTitle(self, title: str) -> str:

        output=[]
        for c in title:
            if c.isupper():
                output.append(chr(ord(c)+32))       #A+32=a
            else:
                output.append(c)         #a
        return ''.join(output)       #convert list to string
        
    


