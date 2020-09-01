winter = [1, 2, 12]
spring = [3, 4, 5]
summer = [6, 7, 8]
autamn = [9, 10, 11]
user_quation = int(input('Введите номер месяца от 1 до 12'))
start_schet = 1
while True:
    if user_quation <= 0 or user_quation > 12:
        user_quation = int(input('Введите номер месяца от 1 до 12'))
    else:
        break
for months_winter in winter:
    if user_quation == months_winter:
        print('Зима')
for months_spring in spring:
    if user_quation == months_spring:
        print('Весна')
for months_summer in summer:
    if user_quation == months_summer:
        print('Лето')
for months_autamn in autamn:
    if user_quation == months_autamn:
        print('Осень')



