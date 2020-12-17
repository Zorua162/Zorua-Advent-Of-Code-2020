'''
Day 1 get the two numbers in input.txt that sum to 2020
'''
with open('./input.txt', 'r') as f:
    data = f.read()

data = data.split('\n')[:-1]

for i in data:
    i = int(i)
    for j in data:
        j = int(j)
        for k in data:
            k = int(k)
            if i + j + k == 2020:
                print(f'{i} + {j} + {k} == 2020')
                print(f'Multiplied == {i * j * k}')
