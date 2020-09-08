from itertools import cycle, count
starting = int(input('Введите старт: '))
for m in count(start=starting):
    if m > 30:
        break
    print(m)
