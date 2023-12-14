# Дано вещественное число — цена 1 кг конфет. Вывести стоимость 1.2, 1.4, ..., 2 кг конфет.

candy_price = input("Введите цену за кг конфет: ")  # Цена за кг

while type(candy_price) != float: # обработка введенных данных пользователем.
    try:
        candy_price = float(candy_price)
    except ValueError:
        print("Вы ввели не тот тип данных! Пожалуйста, введиете снова.\n")
        candy_price = input("Введите цену за кг конфет: ")

for weight in range(12, 21, 2):  # веса от 1.2 до 2.0 кг с шагом 0.2
    print(f"{weight / 10}кг: {(weight / 10) * candy_price}руб")
