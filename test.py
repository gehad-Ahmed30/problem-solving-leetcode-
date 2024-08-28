n=input()
x=n[::-1]
if n[0]=='-':
    print(f"{n[0]}{n[1::-1]}")
print(x)