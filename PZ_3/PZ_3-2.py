num = int(input())

n1 = num // 100
n2 = num % 100

while (n1 >= 1 and n1 <= 4) and (n2 >= 11 and n2 <= 14):
    if n2 == 11:
        print("Валет", end=' ')
    if n2 == 12:
        print("Дама", end=' ')
    if n2 == 13:
        print("Король", end=' ')
    if n2 == 14:
        print("Туз", end=' ')
    if n1 == 1:
        print("пика", end=' ')
    if n1 == 2:
        print("треф", end=' ')
    if n1 == 3:
        print("бубей", end=' ')
    if n1 == 4:
        print("червей", end=' ')
    break
else:
    print("Введите трёхзначное число, первое число которого "
          "будет от 1 до 4, а два других числа от 11 до 14 включительно")
