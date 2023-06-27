x = int(input("Введите x: "))
y = int(input("Введите y: "))
if x > 0:
    if y > 0:  # x>0, y>0
        print("Первая четверть")
    else:
        if y < 0:  # x>0, y<0
            print("Четвертая четверть")
        else:
            print("Точка принадлежит одной из координатных осей")
else:
    if x < 0:
        if y > 0:  # x<0, y>0
            print("Вторая четверть")
        else:
            if y < 0:  # x<0, y<0
                print("Третья четверть")
            else:
                print("Точка принадлежит одной из координатных осей")
    else:
        print("Точка принадлежит одной из координатных осей")

x = int(input("Введите x: "))
y = int(input("Введите y: "))
if x > 0 and y > 0:
    print("Первая четверть")
elif x > 0 and y < 0:
    print("Четвертая четверть")
elif x < 0 and y > 0:
    print("Вторая четверть")
elif x < 0 and y < 0:
    print("Третья четверть")
else:
    print("Точка принадлежит одной из координатных осей")

year = int(input("Insert year and press Enter:"))
if year > 30000:
    print("Year should be <= 30000")
    year = input("Insert year and press Enter:")
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("YES")
else:
    print("NO")
