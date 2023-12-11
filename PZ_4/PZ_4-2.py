n = int(input("Введите число: "))

count = 0
while n > 0:
  count += 1
  n = n // 10

sum = 0


print(f"Количество цифр: {count}")
print(f"Сумма цифр: {sum}")