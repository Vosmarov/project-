numbers = []
numbers_sum = []
while True:
    user_answer = input('Введите любое количество чисел через пробел, если хотите завершить программу, введите [q]: ')
    if user_answer == 'q' or user_answer == 'Q':
        break
    else:
        for number in user_answer.split():
            numbers.append(int(number))
        numbers_sum.append(sum(numbers))
        numbers.clear()
        print(sum(numbers_sum))





