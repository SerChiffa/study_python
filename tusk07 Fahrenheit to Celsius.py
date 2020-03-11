c = ''
far = list(input().split())
s = 0
for i in far[1:]:
    s = round((int(i) - 32)/1.8)
    c += str(s)
    c += ' '
print(c)
