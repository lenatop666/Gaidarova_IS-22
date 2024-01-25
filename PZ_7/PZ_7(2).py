"""
Дана строка-предложение на русском языке и число K (0 < K < 10). Зашифровать
строку, выполнив циклическую замену каждой буквы на букву того же регистра,
расположенную в алфавите на K-й позиции после шифруемой буквы (например, для
K = 2 «А» перейдет в «В», «а» — в «в», «Б» — в «Г», «я» — в «б» и т. д.). Букву «ё»
в алфавите не учитывать, знаки препинания и пробелы не изменять.
"""


def encrypted_string(input_string, k):
    lower = "абвгдежзийклмнопрстуфхцчшщъыьэюя"
    upper = "АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
    result = ""

    for char in input_string:
        if char in lower:
            index = (lower.index(char) + k) % len(lower)
            result += lower[index]
        elif char in upper:
            index = (upper.index(char) + k) % len(upper)
            result += upper[index]
        else:
            result += char
    return result


input_text = str(input("Введите строку-предложение: "))
K = int(input("Введите K(0 < K < 10): "))
text = encrypted_string(input_text, K)
print(text)
