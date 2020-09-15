class Stationery:
    def __init__(self, name):
        self.title = name
    def draw(self):
        return 'Запуск отрисовки...'


painting = Stationery('Канцелярий')

print(painting.draw())


class Pen(Stationery):
    def draw(self):
        return f'{self.title} рисует неплохо...'


pen = Pen('Ручка')
print(pen.draw())


class Pencil(Pen):
    def draw(self):
        return  f'А {self.title} еще лучше...'


pencil = Pencil('карандаш')
print(pencil.draw())


class Handle(Pencil):
    def draw(self):
        return f'Но вот {self.title} неочень....'

handle = Handle('маркер')
print(handle.draw())