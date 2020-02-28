##n=int(input())
##i=1
##while i<=n:
##    if n%i==0:
##        ptint(i, end=' ')
##    i+=1

## или более эффективный способ

n=int(input())
i=1
a=[]
while i*i<=n:##или i<=n**0.5
    if n%i==0:
        a.append(i)
        if i!=n//i:
            a.append(n//i)
    i+=1
a.sort()
print(a)
