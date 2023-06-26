name = input("Введите Ваше имя: ")
age = int(input("Введите Ваш возраст: "))
result = "Ваше имя: "+ name+". Ваш возраст: "+str(age)+"."
print(result)

result = "Ваше имя: %s. Ваш возраст: %i." % (name, age)
print(result)

result = "Ваше имя: %s. Ваш возраст: %s." % (name, age)
print(result)

# ошибочный код
# result = "Ваше имя: %i. Ваш возраст: %s." % (name, age)
# print(result)

height = float(input("Введите Ваш рост (в метрах): "))
result = "Ваш рост: %f м." % height
print(result)

result = "Ваш рост: %.2f м." % height
print(result)

result = f"Ваше имя: {name}. Ваш возраст: {age}. Рост: {height} м"
print(result)
