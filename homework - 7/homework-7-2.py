class Clothing:
    def __init__(self, v, h, v_num, h_num):
        self.title = 'Магазин - Аленушка'
        self.v_palto = v
        self.h_costum = h
        self.cost_palt = None
        self.cost_costum = None
        self.v_zatrats = []
        self.h_zatrats = []
        self.v_num = v_num
        self.h_num = h_num
        self.start = 1

    def formule(self):
        while self.start < self.v_num:
            self.cost_palt = self.v_palto / 6.5 + 0.5
            self.v_zatrats.append(self.cost_palt)
            self.start += 1
        self.start = 1
        while self.start < self.h_num:
            self.cost_costum = 2 * self.h_costum + 0.3
            self.h_zatrats.append(self.cost_costum)
            self.start += 1

    @property
    def sum_cloth(self):
        return sum(self.v_zatrats + self.h_zatrats)


v_palto = float(input('Введите размер пальто: '))
v_count = int(input('Количество пальто: '))
h_costum = float(input('Введите рост костюма: '))
h_count = int(input('Введите кол-во костюмов: '))

clothes = Clothing(v_palto, h_costum, v_count, h_count)
clothes.formule()
print(f'{round(clothes.sum_cloth, 2)} [м] ткани требуется, чтобы сшить одежду')