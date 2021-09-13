name_1 = "Elena"
print("1)", name_1, type(name_1))
name_2 = 56
print("2)", name_2, type(name_2))
name_3 = 2.3
print("3)", name_3, type(name_3))
name_4 = b"hello"
print('4)', name_4, type(name_4))
name_5 = list("hello")
print('5)', name_5, type(name_5))
name_6 = tuple("1,2,3")
print('6)', name_6, type(name_6))
name_7 = set({2,4,2,3,2})
print('7)', name_7, type(name_7))
name_8 = frozenset("hello")
print('8)', name_8, type(name_8))
name_9 = {"world": "мир", "hello": "здравствуй"}
print('9)', name_9, type(name_9))
name_9 = dict(world = "мир", hello = "здравствуй")
print('9)', name_9, type(name_9))

a = "Elena"
b = 'Krupina'
c = a + b
print('11)', c)

d = 49
s = 2
t = d + s
print('12)', t)

d = 49
s = 2
t = d / s
print('13)', t)

d = 49
s = 2
t = d * s
print('14)', t)

d = 49
s = 2
t = d // s
print('15)', t)

d = 49
s = 2
t = d % s
print('16)', t)



