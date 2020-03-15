n = int(input())
b = input()
print(*([sum(int(e)*i for i, e in enumerate(n, start=1)) for n in b.split()]))
