i = 1
while i <= 10:
    print(i)
    i += 1  # i= i+1

x = 2
x *= 4
print(x)

i = 1
while i <= 5:
    note = int(input("Введите оценку: "))
    if note < 60:
        print('НАПРАВЛЕН НА ПЕРЕСДАЧУ')
        break
    i += 1
else:
    print('СТУДЕНТ ЗАКРЫЛ СЕССИЮ БЕЗ ПЕРЕСДАЧ')

n = int(input('Введите натуральное число > 1: '))
d = 1
while n > 1:
    d += 1
    if n % d != 0:
        continue
    print(d, end=' ')
    n /= d
    d -= 1

n = int(input('Введите натуральное число > 1: '))
d = 1
while n > 1:
    d += 1
    if n % d == 0:
        print(d, end=' ')
        n /= d
        d -= 1
