n=(input())
x=[]
for i in n:
    if n.count(i)==3:
        x.append(i)
print(''.join(map(str,x)))

