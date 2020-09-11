with open('newfile.txt') as nf:
    lines = nf.readlines()
    print(lines)
for key, val in enumerate(lines):
    values = val.split()
    print(f'В [{key + 1}] строке - [{len(values)}] слов')