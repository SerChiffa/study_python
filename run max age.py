ages = [1, 0, 12, 25, 34, 432, 234]
ages2 = [2, 34, 65, 4, 62, 73]


def max_age(ages):
    # if len(ages) == 0:
    #	return None   , или написать  так:
    if not ages:
        return

    maximum = ages[0]
    for age in ages:
        if maximum < age:
            maximum = age
    return maximum


print(max_age(ages))
print(max_age(ages2))
print(max_age([]))
