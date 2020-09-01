years_time = {'winter': [1, 2, 12], 'spring': [3, 4, 5], 'summer': [6, 7, 8], 'automn': [9, 10, 11]}
user_answer = int(input('Введите номер месяца'))
while True:
    if user_answer < 1 or user_answer > 12:
        user_answer = int(input('Введите номер месяца'))
    else:
        break
for key, ya_time in years_time.items():
    if user_answer == ya_time[0] or user_answer == ya_time[1] or user_answer == ya_time[2]:
        print(key)
