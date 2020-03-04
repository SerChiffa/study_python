from sys import stdin

#print(sum(int(i) for i in stdin.readlines()[1].split()))

line = input()
symbols = line.split(' ')
sums = 0
for i in symbols:
    digit = int(i)
    sum += digit
print(sums)
