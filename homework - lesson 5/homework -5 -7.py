import json
with open('firms.txt', encoding='utf - 8') as f:
    firms = f.readlines()
name_firms = []
pribyl_firms = []
for firm in firms:
    firmes = firm.split()
    pribyl = int(firmes[2]) - int(firmes[3])
    name_firms.append(firmes[0])
    pribyl_firms.append(pribyl)
board = dict(zip(name_firms, pribyl_firms))
with open('firm.json', 'w') as js:
    json.dump(board, js)