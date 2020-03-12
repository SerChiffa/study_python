result = ''
z = int(input())
res = 0
for i in range(z):
    a, b, n = list(input().split())
    res = (2 * int(a) + (int(n) - 1) * int(b)) * int(n) // 2
    result += str(res)
    result += ' '
print(result)
