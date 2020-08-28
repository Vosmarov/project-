training_max_results = 3.3
training_days = 1
result_day = float(input('Введите результат первого забега [км]'))
while result_day < training_max_results:
    print(f'{training_days} - й день: {result_day} км')
    result_day = result_day / 10 + result_day
    training_days += 1