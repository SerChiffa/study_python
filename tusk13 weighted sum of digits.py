# n = int(input())
# b = input()
# print(*([sum(int(e)*i for i, e in enumerate(n, start=1)) for n in b.split()]))

n = int(input())
s = input().split()
for i in s:
    wsd = 0
    for j in range(len(i)):
        wsd = wsd + int(i[j]) * (j + 1)
    print(wsd, end=' ')
