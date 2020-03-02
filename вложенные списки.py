print('Ниже представлен список "а" и вырианты его обхода')
a = [[0, 2, 4, 6], [1, 3, 5, 7], [10, 20, 30, 40]]
print('a', a)
print('Поочередный обход вложенных списков в списке "a" и вывод каждого вложенного списка с новой строки')
print('for i in a:')
print('    print(i)')
for i in a:
    print(i)
print(' ')
print('Вывод данных вложенных списков в виде таблицы без возможности изменить значения элементов - "a"')
print('for i in a:')
print('    for j in i:')
print('        print(j, end=' ')')
print('        j+=10')
print('    print()')
for i in a:
    for j in i:
        j += 10
        print(j, end=' ')
    print()
print(a)
print('Изменились только значения в "j" на +10 от списка "а", значения в списке "a" остались неизменны')
print(' ')
print('Обход по индексам вложенных массивов с возможностью изменения значений элементов в "а"')
print('for i in range(3):')
print('    for j in range(4):')
print('        #a[i][j] += 10')
print('        print(a[i][j], end=' ')')
print('    print()')
print('print(a)')
for i in range(3):
    for j in range(4):
        #a[i][j] += 10
        print(a[i][j], end=' ')
    print()
print(a)
print('Есле раскоментировать строчку "a[i][j] += 10", то все значения списка "а" изменятся на +10')
print(' ')
print('Обход по индексам с выводом значений по столбцам. Берется сначала индекс 0 из каждого вложенного списка и '
      'выводится, на следующую строчку индекс 1 и так далее')
print('for j in range(4):')
print('    for i in range(3):')
print('        print(a[i][j], end=' ')')
print('    print()')
print('print(a)')
for j in range(4):
    for i in range(3):
        print(a[i][j], end=' ')
    print()
print(a)
print(' ')
print('Обход по индексам вложенных списков в обратном порядке')
print('for i in range(2, -1, -1):')
print('    for j in range(3, -1, -1):')
print('        print(a[i][j], end=' ')')
print('    print()')
print('print(a)')
print('for i in range(2, -1, -1):')
print('    for j in range(3, -1, -1):')
print('        print(a[i][j], end=' ')')
print('    print()')
print('print(a)')
for i in range(2, -1, -1):
    for j in range(3, -1, -1):
        print(a[i][j], end=' ')
    print()
print(a)
print(' ')

