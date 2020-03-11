# n = int(input())
# for i in range(1, n):
#    print(min(map(int, input().split())), end=' ')

# или используя более правильно:

# print(*(str(min(map(int, input().split()))) for _ in range(int(input()))), sep=' ')

# с использованием оператора сравнения

n = int(input())
a = ''
for i in range(n):
    l, r = list(input().split())
    if int(l) < int(r):
        a += l
    else:
        a += r
    a += ' '
print(a)
