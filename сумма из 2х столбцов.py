a = []
n = int(input())
for i in range(n):
    new_column = input().split()
    s = 0
    for j in range(0, len(new_column)):
        s += int(new_column[j])
    a.append(s)
print(a)
