with open('worker.txt', encoding='utf - 8') as wr:
    wr.seek(0)
    worker = wr.readline()


class Position:
    def __init__(self):
        self.get_full_name = {'Name': 'Имя', 'Surname': 'Фамилия', 'Position': 'Должность', 'Income': 'Доход',
                              'Bonus': 'Премия'}
        self.__arguments = worker.split(' - ')


about_worker = Position()

for num, key in enumerate(about_worker.get_full_name.keys()):
    about_worker.get_full_name[key] = about_worker._Position__arguments[num]
print(about_worker.get_full_name)
