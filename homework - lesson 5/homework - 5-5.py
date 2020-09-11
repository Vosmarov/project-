from functools import reduce
def funcplus(x_num, y_num):
    sum = x_num + y_num
    return sum
with open('nums.txt', 'w+', encoding='utf-8') as nums:
    number = input('Введите числа через пробел: ')
    numbers = []
    for num in number.split():
        numbers.append(int(num))
    print(reduce(funcplus, numbers))
    nums.write(f'{number}\nСумма чисел = {reduce(funcplus, numbers)}')
