s=input()
output=[]
s=s.lower()
for char in s:
        if char.isalpha() or char.isnumeric():
            output.append(char)
        result=''.join(map(str,output))
if result==result[::-1]:
      print("yes")