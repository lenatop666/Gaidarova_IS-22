"""
Дан список размера N. Обнулить все его локальные максимумы (то есть числа,
большие своих соседей).
"""
import random


def nullify_local_maxima(lst):
    new_lst = lst.copy()
    for i in range(1, len(lst) - 1):
        if lst[i] > lst[i - 1] and lst[i] > lst[i + 1]:
            new_lst[i] = 0
    return new_lst


N = int(input("Введите N размер списка: "))
A = [random.randint(1, 10) for i in range(N)]
result = nullify_local_maxima(A)
print("До:   ", A)
print("После:", result)
