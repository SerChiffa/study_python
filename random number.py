import random

ages = [random.randint(0, 100) for i in range(20)]
# или способом ниже:
# ages = []
# for i in range(21):
#	ages.append(random.randint(0, 100,))

print(ages)
print(max(ages))
