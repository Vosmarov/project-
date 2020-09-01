count_massive = int(input('Введите желаемую длину списка (Максимум 5 значений)'))
while True:
    if count_massive <= 0 or count_massive > 5:
        count_massive = int(input('Пожалуйста, введите длину от 1 до 5 (Максимум 5 значений)'))
    else:
        user_list = []
        start_schets = 1
        reverse_list = []
        break
while start_schets <= count_massive:
    user_answers = input(f'Введите любой набор букв/слово или цифру/число [{start_schets}]')
    user_list.append(user_answers)
    start_schets += 1
if count_massive % 2 == 1:
    reverse_list.append(user_list[-1])
else:
    user_list = user_list[0:]
print(user_list)
start_schets = 1
user_list.clear()
while start_schets <= count_massive:
    user_answer_reverse = input(f'Введите значение на замену [{start_schets}]')
    start_schets += 1
    reverse_list.insert(0, user_answer_reverse)
print(reverse_list)




