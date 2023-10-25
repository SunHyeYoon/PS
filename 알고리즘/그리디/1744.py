import sys

n = int(input())

minus = []
plus = []
zero = []

for _ in range(n):
    i = int(input())
    if i < 0:
        minus.append(i)
    elif i == 0:
        zero.append(i)
    else:
        plus.append(i)

plus.sort(reverse=True)
minus.sort()
sm = []

for x, y in zip(plus[0::2], plus[1::2]):
    if x == 1 or y == 1:
         continue
    plus.remove(x)
    plus.remove(y)
    sm.append(x * y)
sm.extend(plus)

for x, y in zip(minus[0::2], minus[1::2]):
    minus.remove(x)
    minus.remove(y)
    sm.append(x * y)

if minus and not zero:
        sm.append(minus[0])

print(sum(sm))
