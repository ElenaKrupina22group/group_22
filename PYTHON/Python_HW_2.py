

name = 'elena'
surname = 'krupina'
a = 33
b = 10
c = 5
d = -8
f1 = 2.5
f2 = 30.3
f3 = 100.55

print(a<b, a>b, a>=b, a<=b, a!=b, c<d, c>d, c<=d, c>=d, c!=d, a<d, b>c, a!=d, c>=b, b!=c)

print(f1<f2, f1>f2, f1!=f2, f2<=f3, f2>=f3, f2!=f3, f1<f3, f1>=f3, f1!=f3)

ok1 = a<b and c>d
ok2 = a<=d or a!=c
ok3 = a!=b and c<=d
ok4 = d>b or b>=a
ok5 = c!=b and c>d
ok6 = b>c or b!=a
ok7 = d>=c and d<a
ok8 = not a<b
ok9 = not c>=d
ok10 = not d!=a

print(ok1, ok2, ok3, ok4, ok5, ok6, ok7, ok8, ok9, ok10)

name = int(input('Введите число: '))
if name > 30:
    print('Вы ввели число ', name, ',',  'которое', ">30")
elif name < 30:
    print('Вы ввели число ', name, ',', 'которое', "<30")
else:
    print('Вы ввели число ', name, ',', 'которое', "=30")


import random
name = int(input('Введите число: '))
r1 = random.randint(1,100)
x1 = ">"
x2 = "<"
x3 = "="
if name > r1:
     x = x1
elif name < r1:
     x = x2
else: x = x3
print('Вы ввели число =', name, ',',  'которое', x, r1)

name = int(input('Введите число: '))
r1 = random.randint(1,100)
r2 = random.randint(1,100)
x1 = ">"
x2 = "<"
x3 = "="
if name > r1:
     x = x1
elif name < r1:
     x = x2
else: x = x3
if name > r2:
     y = x1
elif name < r2:
     y = x2
else: y = x3

print('Вы ввели число =', name, ',',  'которое', x, r1, 'и', y, r2)


