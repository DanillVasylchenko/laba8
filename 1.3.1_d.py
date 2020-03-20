'''
Y матриці 4*4, що задана користувачем замініть всі від’ємні елементи на 0.
Васильченко Даниїл Назарович 122 А
'''
import numpy as np

zero_matrix = np.zeros((4, 4), dtype=int)
while True:
    try:
        for i in range(4):
            for k in range(4):
                zero_matrix[i][k] = int(input(f'Введіть елемент [{i + 1},{k + 1}] вашої матриці:'))

                if zero_matrix[i, k] < 0:
                    zero_matrix[i, k] = 0
        break
    except ValueError:
        print("Введіть число!")
print(f'Оновлена нулями матриця{zero_matrix}')
