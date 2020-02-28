a=int(input())
if a<0 or a>=10000:
    print('error')
elif a<10:
    if a%2==0:
        print('1 число четное')
    else:
        print('1 число нечетное')
elif a<100:
    if a%2==0:
        print('2 числа четное')
    else:
        print('2 числа нечетное')
elif a<1000:
    if a%2==0:
        print('3 числа четное')
    else:
        print('3 числа нечетное')
elif a<10000:
    if a%2==0:
        print('4 числа четное')
    else:
        print('4 числа нечетное')
