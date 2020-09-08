import random, functools
def my_f(x, y):
    if x < y:
        return y
    elif x > y:
        return x
first_list = []
schets_end = 10
schets_start = 1
while schets_start <= schets_end:
    first_list.append(random.randint(1, 1000))
    schets_start += 1
print(first_list)
last_list = []
while schets_start <= schets_end:
    last_list.append(functools.reduce(my_f, first_list))
print(last_list)