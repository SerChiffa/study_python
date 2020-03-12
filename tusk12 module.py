n = int(input())
answer = ''
for calculation in range(n):
    solution = 0
    # d - Day, h - hour, m - minute,s - second:
    d1, h1, m1, s1, d2, h2, m2, s2 = map(int, list(input().split()))

    if s2 >= s1:
        s = s2 - s1
    else:
        m2 -= 1
        s2 += 60
        s = s2 - s1

    if m2 >= m1:
        m = m2 - m1
    else:
        h2 -= 1
        m2 += 60
        m = m2 - m1

    if h2 >= h1:
        h = h2 - h1
    else:
        d2 -= 1
        h2 += 24
        h = h2 - h1
    d = d2 - d1
    answer += ('(' + str(d) + ' ' + str(h) + ' ' + str(m) + ' ' + str(s) + ') ')
print(answer)
