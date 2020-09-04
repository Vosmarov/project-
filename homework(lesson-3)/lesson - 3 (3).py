number_list = []
schets = 1
max_schets = 3
while schets <= max_schets:
    user_answer = int(input(f'Пожалуйста, введите [{schets}] число:'))
    number_list.append(user_answer)
    schets += 1
number_list.remove(min(number_list))
print(sum(number_list))