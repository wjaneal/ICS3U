b = ord("^")
print(b)
c = ord("+")
print(c)
d = ord("x")
print(d)
a = "33x^3+22x^1+1"
Separate = []
plus = []
term = []
x = []
result = ""
n = 1
for i in a:
    Separate.append(i)
print(Separate)
for order in range(0,len(Separate)):
    if ord(Separate[order]) == 43:
        plus.append(order)
        n = n+1
    if ord(Separate[order]) == 120:
        x.append(order)
print(n)
print(plus)
print(x)
