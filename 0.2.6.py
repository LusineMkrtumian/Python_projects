a_list = [2, 1, 0, -7, 3.14, 2.7, 5]
v = -3.14
for a in a_list:
    if v == a:
        print('Элемент найден')
        break
else:
    print('Элемент не найден')
