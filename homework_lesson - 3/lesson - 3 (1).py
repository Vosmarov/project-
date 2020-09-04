def my_func(x_num, y_num):
    try:
        z_num = x_num / y_num
    except ZeroDivisionError:
        z_num = float(0)
    return z_num
schets = 1
user_answer_x = int(input(f'Введите число [{schets}]'))
schets += 1
user_answer_y = int(input(f'Введите число [{schets}]'))
z_number = my_func(user_answer_x, user_answer_y)
print(z_number)
