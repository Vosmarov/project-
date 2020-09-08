from itertools import cycle
my_list = ['Самый', ' ', 'лучший', ' ', 'день']
for el in cycle(my_list):
    print(el)