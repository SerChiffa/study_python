##a = [43, 54, 43, 65, 3, 76]
##count = 0
##обход по значениям, при совпадающих значениях выводит индекс первого
##for i in a:
##    print(i, a.index(i))

##обход по индексам
##n = len(a)
##for i in range(n):
##    print(i, a[i])
##    a[i] +=5
##print(a)

a = [1, 2, 3, 4, 32, 4, 5, 3, 5]
##b = []
##for i in a:
##    if not i  in b:
##        b.append(i)
##print(b)
## на каом месте по индексу четные и нечетные:
chet = []
nechet = []
n = len(a)
for i in range(n):
    if a[i]%2==0:
        chet.append(i)
    else:
        nechet.append(i)
print(chet)
print(nechet)
