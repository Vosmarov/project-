type_inform = ['Имя', 'Фамилия', 'Год рождения', 'Город проживания', 'Email', 'Phone']
user_inform = []
for inform in type_inform:
    user_answer = input(inform)
    user_inform.append(user_answer)
print(dict(zip(type_inform, user_inform)))
