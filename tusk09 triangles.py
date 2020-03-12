n = int(input())
result = ''
for i in range(n):
    #a, b, c = list(input().split())
    #if int(a) + int(b) >= int(c) and int(a) + int(c) >= int(b) and int(b) + int(c) >= int(a):
    #или более лучшим вариантом:
    a, b, c = map(int, list(input().split()))
    if a + b >= c and a + c >= b and b + c >= a:
        result += str(1)
    else:
        result += str(0)
    result += ' '
print(result)
