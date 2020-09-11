with open('numbers.txt', 'r+', encoding='utf-8') as num:
    eng_num = num.readlines()
    print(eng_num)
    rus_num = []
    for val in eng_num:
        values = val.split('-')
        if values[0] == 'one':
            values[0] = 'один'
        elif values[0] == 'two':
            values[0] = 'два'
        elif values[0] == 'three':
            values[0] = 'три'
        elif values[0] == 'four':
            values[0] = 'четыре'
        rus_num.append('-'.join(values))
    num.seek(0)
    num.write(''.join(rus_num))

