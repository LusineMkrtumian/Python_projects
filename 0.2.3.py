s = 'Take a look around'
for c in s:
    print(c)

x = [1, 2, 3, 4]
total = 0
for i in x:
    total += i
print(total)

x = (1, 2, 3, 4, 7, 49, 4, 23, 63, 28, 28)
total = 0
for i in x:
    if i % 7 == 0:
        total += i
print(total)

x_set = set(x)
total = 0
for i in x_set:
    if i % 2 == 0:
        total += i
print(total)
print(x_set)
