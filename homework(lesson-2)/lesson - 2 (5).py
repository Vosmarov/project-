users_competition = [3, 2, 1]
schets = 1
number_players = int(input('Введите количество участников: '))
while schets <= number_players:
    for ratings in users_competition:
        user_rating = int(input(f'Введите место рейтинга участника [{schets}]: '))
        if user_rating == ratings:
            users_competition.insert(users_competition.index(ratings) + 1, user_rating)
            break
        else:
            users_competition.insert(0, user_rating)
            break
    schets += 1
    print(users_competition)

