a = True; b = 3 < 2
print(a)
print(b)

s1 = bool("")  # 0, None или пустая последовательность преобразуются в False
s2 = bool("Hello world!")
print(s1); print(s2)

x = 0  #  - 0, None или пустая последовательность преобразуются в False
if x:
    print(f"Число {x} отлично от 0")
else:
    print("Нулевое значение")

a = int(input("Введите число: "))
if a % 7 == 0:
    print(a)
    print("ДА")
else:
    print("НЕТ")


