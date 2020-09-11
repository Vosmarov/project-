from functools import reduce
with open('paywork.txt') as pw:
    workers = pw.readlines()
def my_f(x_num, y_num):
    z_num = x_num + y_num
    return z_num
paywork = []
normal_workers = []
for worker in workers:
    wr = worker.split()
    paywork.append(int(wr[1]))
    if int(wr[1]) > 20000:
        normal_workers.append(wr[0])
print(f'Средняя зарплата: {reduce(my_f, paywork) // len(paywork)} $')
norm = ', '.join(normal_workers)
print(f'Рабочие, имеющие оклад больше 20000 $: {norm}')