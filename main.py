import random

a = []
b = 1

for i in range(100000):
    a.append(random.randint(0, 1))

a_string = [str(i) for i in a]
a_numb = int("".join(a_string))

while str(b) in str(a_numb):
    b = str(b) + '1'

print(len(str(b))-1)

print(f'Одиниць — {a.count(1)}')
print(f'Нулів — {a.count(0)}')
