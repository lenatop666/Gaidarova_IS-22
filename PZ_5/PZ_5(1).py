"""
С помощью функций получить вертикальную и горизонтальную линии. Линия
проводится многократной печатью символа. Заключить слово в рамку из
полученных линий.
"""


def hz(width, symbol):
    return symbol * width


def vt(word, height, symbol):
    lines = []
    for i in range(height):
        if i == height // 2:
            lines.append(f'{symbol} {word} {symbol}')
        else:
            lines.append(f'{symbol}{" " * (len(word) + 2)}{symbol}')
    return "\n".join(lines)


def create_frame(word, symbol, height):
    width = len(word) + 4
    height = height
    hz_line = hz(width, symbol)
    vt_line = vt(word, height, symbol)
    frame = hz_line + '\n' + vt_line + '\n' + hz_line
    return frame

word = input("Введите ваше слово: ")
symbol = input("Введите символ для рамки: ")
height = int(input("Задайте высоту для рамки: "))

frame = create_frame(word, symbol, height)
print(frame)

