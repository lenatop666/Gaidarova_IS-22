"""
Дано целое число N (1 < N < 26). Вывести N последних строчных (то есть маленьких)
букв латинского алфавита в обратном порядке (начиная с буквы «z»).
"""

import string


def print_last_chars(n):
    if 1 < n < 26:
        chars = string.ascii_lowercase
        print(f"латинский алфавит наоборот:\n{chars[::-1]}")
        last_chars = chars[-n:][::-1]
        print(last_chars)
    else:
        print("1 < N < 26")


N = int(input("Введите N : "))
print_last_chars(N)
