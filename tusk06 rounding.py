n = int(input())
a = ''
for i in range(n):
    l, r = list(input().split())
    result = round(int(l) / int(r))
    a += str(result)
    a += ' '
print(a)
