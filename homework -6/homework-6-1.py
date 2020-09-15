from time import sleep


class TrafficLights:
    def __init__(self):
        self.__colors = ['Красный', 'Желтый', 'Зеленый']
        self.start_lights = print('Запуск...')


traffic = TrafficLights()
traffic.start_lights


while True:
    for color in traffic._TrafficLights__colors:
        print(color)
        sleep(3)