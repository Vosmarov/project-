user_seconds = int(input('Введите количество секунд'))
hour = user_seconds // 3600
minutes = (user_seconds % 3600) // 60
seconds = (user_seconds % 3600) % 60
print(hour, minutes, seconds)