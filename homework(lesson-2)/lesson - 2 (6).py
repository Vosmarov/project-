analytik_woods = []
number_wood = 1
count_woods = int(input('Введите общее количество товаров'))
while number_wood <= count_woods:
    woods_name = input(f'Введите название товара [{number_wood}]')
    cost = int(input(f'Введите цену товара [{number_wood}]'))
    count = int(input(f'Введите количество товара [{number_wood}]'))
    num = input(f'Введите единицу измерения товара [{number_wood}]')
    wood = (number_wood, {'Название': woods_name, 'Цена': cost, 'Количество': count, 'Ед': num})
    analytik_woods.append(wood)
    number_wood += 1
for analytik in analytik_woods:
    print(analytik)