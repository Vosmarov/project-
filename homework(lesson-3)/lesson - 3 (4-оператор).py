def my_func(x_num, y_num):
    try:
        num = 1 / x_num ** abs(y_num)
    except ZeroDivisionError:
        num = float(0)
    return num
x_number = float(input('Введите действительное число x:'))
y_number = int(input('Введите целое отрицательное число y'))
while True:
    if y_number >= 0:
        y_number = int(input('Введите целое отрицательное число y'))
    else:
        break
stepen = my_func(x_number, y_number)
print(round(stepen, 4))