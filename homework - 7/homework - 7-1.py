from random import randint


class Matrix:
    def __init__(self, max_num, min_num):
        self._max_num = max_num
        self.start_num = min_num
        self.matrix_list = []

    def randomizer(self):
        while self.start_num <= self._max_num:
            random_list.append(randint(1, 10))
            self.start_num += 1
        self.start_num = self._max_num - self.start_num
        all_matrix.append(random_list)


    def matrix_split(self):
        return ' '.join(self.matrix_list).strip()

    def __add__(self, other):
        pass

    def __str__(self):
        return self.matrix_list


while True:
    user_answer_nim = int(input('Введите минимальную длину матрицы: '))
    user_answer_max = int(input('Введите максимальную длину матрицы: '))
    if user_answer_nim > user_answer_max:
        print('Минимальное значение не может быть больше максимального!')
    elif user_answer_max % 3 == 1:
        print('Максимальное значение должно быть кратным трем!')
    else:
        break

matrix = Matrix(user_answer_max, user_answer_nim)
start_schets = 1
random_list = []
all_matrix = []

while start_schets <= 3:
    matrix.randomizer()
    start_schets += 1

print(all_matrix)


