ages = [1, 0, 12, 25, 34, 432, 234]
# print(max(ages))

# maximum = ages[0]
# for age in ages:
#	print(maximum, age, maximum < age) - выводит булеевое значение сравнения
#	if maximum < age:
#		maximum = age
# print(maximum)

maximum = ages[0]
i = 0
while i < len(ages):
    if maximum < ages[i]:
        maximum = ages[i]
    i += 1
print(maximum)
