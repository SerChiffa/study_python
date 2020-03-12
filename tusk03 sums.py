from sys import stdin
#print(sum(int(i) for i in stdin.readlines()[1].split()))

#line = input()
#symbols = line.split(' ')
#sums = 0
#for i in symbols:
#    digit = int(i)
#    sums += digit
#print(sums)

line1 = input()
line2 = input().split()
s = 0
for i in range(0, len(line2)):
    s += int(line2[i])
print(s)
