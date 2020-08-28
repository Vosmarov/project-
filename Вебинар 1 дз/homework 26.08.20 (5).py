balance_vrch = int(input('Введите значение выручки фирмы'))
balance_izderj = int(input('Введите значение издержки фирмы'))
if balance_vrch > balance_izderj:
    print('Ваша фирма в этот раз имеет прибыль')
    balance_pribyl = balance_vrch - balance_izderj
    rentable = balance_pribyl / balance_vrch
    print(f'Рентабельность выручки составляет {rentable} единиц')
    count_workers = int(input('Введите количество сотрудникой вашей фирмы'))
    pribyl_workers = balance_pribyl // count_workers
    print(f'Прибыль фирмы в расчете на одного сотрудника составляет {pribyl_workers}')
elif balance_vrch < balance_izderj:
    print('Ваша прибыль потерпела убытки')
