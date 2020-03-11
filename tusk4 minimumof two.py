#n = int(input())
#for i in range(1, n):
#    print(min(map(int, input().split())), end=' ')

#или используя более правильно:

print(*(str(min(map(int, input().split()))) for _ in range(int(input()))), sep=' ')
