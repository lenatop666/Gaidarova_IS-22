"""
Дан список A размера N и целые числа K и L (1 < K < L < N). Переставить в обратном
порядке элементы списка, расположенные между элементами AK и AL, включая эти
элементы.
"""


def reverse_sublist(a, k, l):
    if 1 < k < l < len(a):
        a[k - 1:l] = reversed(a[k - 1:l])
    else:
        print("Ошибка: проверьте значения K и L.")
    return a


N = int(input("Введите N размер списка: "))
print("Введите 2 целых числа (1 < K < L < N)")
K = int(input("Введите K: "))
L = int(input("Введите L: "))
A = list(range(1, N + 1))

result = reverse_sublist(A, K, L)
print("Измененный список:", result)
