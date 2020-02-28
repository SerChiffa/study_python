##Алгоритм Евклида для нахождения НОД:

##a=int(input())
##b=int(input())
##while a!=b:
##    if a>b:
##        a=a-b
##    else:
##         b=b-a
##print(a)
##или написать так, что быстрее выведет результат

##a,b = map(int, input().split())
##while a!=b:
##    if a>b:
##        a=a-b
##    else:
##         b=b-a
##print(a)
##  или найти НОД таким способом


a, b = map(int, input().split())  ##или можно записать так:
##a=int(input())
##b=int(input())
while b > 0:
    a, b = b, a % b
print(a)
