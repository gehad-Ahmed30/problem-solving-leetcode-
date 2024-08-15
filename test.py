n=int(input())
summ=0
for i in range(n):
    for j in range(i+1,n):
        if i+j == n:
            summ+=1
print(summ)
            
