from functools import reduce
def my_fnc(x_num, y_num):
    z_num = x_num + y_num
    return  z_num
print(reduce(my_fnc, range(100, 1000)))