from random import randint
from time import sleep


common_colors = ['black', 'white', 'blue', 'red']

cars_name = ['volga', 'merz', 'volva', 'bently']


class Car:
    def __init__(self):
        self.color = common_colors[randint(0, len(common_colors) - 1)]
        self.name = cars_name[randint(0, len(cars_name) - 1)]
        self.go = f'Машина {self.name}, цвет - {self.color} завелась успешно и начала свой путь!'
        self.stop = 'Машина остановилась!'
        self.direction = 'Машина повернула'


class SportCar(Car):
    def show_speed(self):
        speed = randint(30, 90)
        return speed
    def show_oil(self):
        oil = randint(50, 120)
        return oil


car = Car()

sport_car = SportCar()


start_speed = sport_car.show_speed()
print(car.go)
print(f'Начальная скорость: {start_speed} км/ч')
sleep(3)

car_oil = sport_car.show_oil()
car_way = 0

while True:
    finish_speed = sport_car.show_speed()
    random_direction = randint(40, 180)
    if random_direction > 115:
        if start_speed < finish_speed:
            car_way = round(car_way + (((start_speed + (finish_speed - start_speed))/3600.0) * 3.0), 2)
            print(f'{car.direction} направо на [{180 - random_direction}] градусов, ускорившись на '
                  f'{finish_speed - start_speed} км/ч,\n Пройденный путь: {car_way} [км]')
            start_speed = finish_speed
            car_oil = round(car_oil - (((start_speed * 0.3) / 3600.0) * 3), 2)
            print(f'Осталось топлива: {car_oil}')
            sleep(3)
        else:
            car_way = round(car_way + (((start_speed - (start_speed - finish_speed))/3600.0) * 3.0), 2)
            print(f'{car.direction} направо на [{180 - random_direction}] градусов, замедлившись на {start_speed - finish_speed} км/ч\n'
                  f'Пройденный путь: {car_way} [км]')
            start_speed = finish_speed
            car_oil = round(car_oil - (((start_speed * 0.3) / 3600.0) * 3), 2)
            print(f'Осталось топлива: {car_oil}')
            sleep(3)
    elif random_direction < 75:
        if start_speed < finish_speed:
            car_way = round(car_way + (((start_speed + (finish_speed - start_speed)) / 3600.0) * 3.0), 2)
            print(f'{car.direction} налево на [{75 - random_direction}] градусов, ускорившись на '
                  f'{finish_speed - start_speed} км/ч,\n Пройденный путь: {car_way} [км]')
            start_speed = finish_speed
            car_oil = round(car_oil - (((start_speed * 0.3) / 3600.0) * 3), 2)
            print(f'Осталось топлива: {car_oil}')
            sleep(3)
        else:
            car_way = round(car_way + (((start_speed - (start_speed - finish_speed)) / 3600.0) * 3.0), 2)
            print(f'{car.direction} налево на [{75 - random_direction}] градусов, замедлившись на {start_speed - finish_speed} км/ч\n '
                  f'Пройденный путь: {car_way} [км]')
            start_speed = finish_speed
            car_oil = round(car_oil - (((start_speed * 0.3) / 3600.0) * 3), 2)
            print(f'Осталось топлива: {car_oil}')
            sleep(3)
    elif random_direction > 75 and random_direction < 115:
        car_way = round(car_way + ((start_speed / 3600.0)) * 3.0, 2)
        print(f'Машина едет прямо, с одной и той же скоростью\n Пройденный путь: {car_way} [км]')
        car_oil = round(car_oil - (((start_speed * 0.3) / 3600.0) * 3), 2)
        print(f'Осталось топлива: {car_oil}')
        sleep(3)
    elif car_oil <= 0:
        print(f'Топливо кончилось!{car.stop}')
        break

