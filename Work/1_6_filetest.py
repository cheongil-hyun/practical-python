""" import os
print(os.getcwd())

with open('Data/portfolio.csv', 'rt') as f :
    headers = next(f)
    print(headers, end='')
    for line in f:
        print(line, end='')
 """

import os
print(os.getcwd())

with open('Data/portfolio.csv', 'rt') as f :
    total_cost = 0 
    headers = next(f).split(',')
    print(headers)
    for line in f:
        row = line.split(',')
        print(row)
        total_cost += int(row[1]) * float(row[2])

    print('Total cost ', round(total_cost, 2))
