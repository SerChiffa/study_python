#проще
#print(*(str(min(map(int, input().split()))) for _ in range(int(input()))), sep=' ')

#или используя оператор сравнения:
n = int(input())
a = ''
for i in range(n):
    l, m, r = list(input().split())
    if int(l) < int(m) and int(l) < int(r):
        a += l
    elif int(l) > int(m) and int(m) < int(r):
        a += m
    else:
        a += r
    a += ' '
print(a)
