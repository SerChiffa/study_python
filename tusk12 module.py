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

# или более короткая версия:
#n = int(input())
#for i in range(n):
#    a = list(map(int, input().split()))
#    b = a[4] * 24 * 60 ** 2 + a[5] * 60 ** 2 + a[6] * 60 + a[7] - (
#                a[0] * 24 * 60 ** 2 + a[1] * 60 ** 2 + a[2] * 60 + a[3])
#    print("(%s %s %s %s)" % (b // (24 * 60 ** 2), b // 3600 % 24, (b // 60) % 60, b % 60), end=' ')
