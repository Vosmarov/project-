with open('facultetes.txt', encoding='utf - 8') as fac:
    facultes = fac.readlines()
finish_projects = []
finish_fac = []
f =[]
for facult in facultes:
    print(facult)
    facult_list = facult.split()
    finish_projects.append(facult_list[0])
    for val in facult_list:
        try:
            values = int(val)
            finish_fac.append(values)
        except ValueError:
            values = str(val)
            f.append(values)
print(finish_projects)
print(dict(zip(finish_projects, sum_fac)))




