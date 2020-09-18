from random import randint

class Cell:
    def __init__(self, count, tabel):
        self.count_cell = count
        self.cell_tabel = tabel
        self.i = 1
        self.sum = None

    def __add__(self, other):
        self + other
        return self

    def __sub__(self, other):
        if len(self) < len(other):
            return self - other
        else:
            return other - self



    @property
    def celling(self):
        cell_count = []
        share_count = self.count_cell * self.cell_tabel
        while self.i <= share_count:
            if self.i == self.count_cell:
                cell_count.append('*\n')
                self.i += 1
                self.count_cell += self.count_cell
            else:
                cell_count.append('*')
                self.i += 1
        self.i = 1
        return cell_count

cell_one = Cell(randint(1, 10), randint(1, 3))
cell_two = Cell(randint(1, 10), randint(1, 3))
celling_1 = cell_one.celling
celling_2 = cell_two.celling


