# Дано целое число N (>0). Используя операции деления нацело и взятия остатка от деления, найти количество и сумму его цифр.

number = input("Введите N: ")

while type(number) != int: # обработка введенных данных пользователем.
    try:
        number = int(number)
    except ValueError:
        print("Вы ввели не тот тип данных! Пожалуйста, введиете снова.\n")
        number = input("Введите N: ")

while number < 0:
    print("N > 0")
    number = int(input("Введите N: "))

digits_count, digits_sum = 0, 0

while number > 0:
    digits_sum += number % 10
    digits_count += 1
    number //= 10

print(f"Количество цифр: {digits_count}\nСумма цифр: {digits_sum}")
