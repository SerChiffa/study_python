n = int(input())
res = ''

for i in range(n):
    a, b, c = map(int, list(input().split()))
    d = (a * b) + c
    d = str(d)
    s = 0
    for j in d:
        s += int(j)
    res += str(s)
    res += ' '
print(res)
