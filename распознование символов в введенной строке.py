s='heLlo3 wOrLd!'
##while len(s)>0:
##    symbol=s[0]
##    if symbol>='a' and symbol<='z':
##        print(symbol, 'small letter')
##    elif symbol>='A' and symbol<='Z':
##        print(symbol, 'big letter')
##    elif symbol.isdigit():
##        print(symbol, 'digit')
##    else:
##        print(symbol, 'sign')
##    s=s[1:]

## ИЛИ через цикл for:

for i in s:
    if 'a'<=i<='z':
        print(i, 'small letter')
    elif 'A'<=i<='Z':
        print(i, 'big letter')
    elif i.isdigit():
        print(i, 'digit')
    else:
        print(i, 'symbol')
