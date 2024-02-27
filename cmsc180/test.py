import random
matrix = []

for j in range(0,1000):
    for i in range(0, 1000):
        matrix.append(random.randint(0, 1000*1000))

print(matrix)