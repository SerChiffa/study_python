n = int(input())
res = ''


def linear(p1, p2):
    dx = p2[0] - p1[0]
    dy = p2[1] - p1[1]
    return dy / dx, (p2[0] * p1[1] - p1[0] * p2[1]) / dx


for i in range(n):
    x1, y1, x2, y2 = map(int, list(input().split()))
    a, b = linear((x1, y1), (x2, y2))
    res += '({0:.0f} {1:.0f})'.format(a, b)
    res += ' '
print(res)
