from math import factorial
def n_func(n):
    for mk_fac in range(1, n + 1):
        yield factorial(mk_fac)
n_fac = int(input('Введите n-количество факториалов: '))
for generator in n_func(n_fac):
    print(generator)