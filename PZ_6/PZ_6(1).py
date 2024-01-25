"""
Дано целое число N (>2). Сформировать и вывести целочисленный список размера
10, содержащий 10 первых элементов последовательности чисел Фибоначчи
FK: F1 = 1, F2 = 1, FK = FK-2 + FK-1, K = 3,4,...
"""


def sequence(n):
    fibanachi = [0, 1]

    while len(fibanachi) < n:
        next_fib = fibanachi[-1] + fibanachi[-2]  # FK = FK-2 + FK-1
        fibanachi.append(next_fib)

    return fibanachi


N = 10
fibonachi_list = sequence(N)
print(f"Первые {N} элементов последовательности Фибоначчи: {fibonachi_list}")
