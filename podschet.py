a = []
import random

for i in range(10):
    a.append(random.randint(-10, 10))  # добавляем в конец списка 'a' случайное число от -10 до 10
count = [0] * 21
for i in a:
    count[i + 10] += 1  # используем смещение на 10
print(a)
for i in range(21):
    if count[i] > 0:
        print(i - 10, count[i])  # нейтрализум используемое ранее смещение и выводим результат подсчета

# Подсчет повторяющихся букв:
s = 'f][sdzxcglgavc,aaferdkloo;.;sdqw2gs /gfgaw'
letters = [0] * 26  # 26 букв английского алфавита
for i in s.lower():  # преводим буквы в нижний регистр
    if 'a' <= i <= 'z':  # отсекаем все символы и оставляем буквы
        nomer = ord(
            i) - 97  # переводим букву к порядковому номеру кодировки ASCII и смещаем на -97, чтоб у 'a' был 0 порядковый номер
        letters[nomer] += 1  # проихводим подсчёт повторяющихся символов

for i in range(26):
    if letters[i] >= 0:
        # print(chr(i+97), letters[i]) - возвращаем цифры в к изначельной кодировке предварительно нейтрализуя смещение и выводим на экран
        print(chr(i + 97) * letters[i],
              end='')  # то же что и выше + выводим отсротировано в одну строку без пробелов буквы

# подсчет повторов цифр в массиве
# a = [0, 3, 1, 0, 2, 3, 1, 3, 5, 5, 2, 0, 4, 1, 3, 5, 1, 2, 2]
# count = [0] * 6
# for i in a:
#    count[i] += 1
# print(count)
# for i in range(6):
#    print(i, count[i])
