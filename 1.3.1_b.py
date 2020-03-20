'''
виведіть на екран транспоновану матрицю 3*3 (початкова матриця задана
користувачем).
Васильченко Даниїл Назарович 122 А
'''
import numpy as np
while True:
    try:
        zero_matrix = np.zeros((3, 3), dtype=int)
        for i in range(3):
            for k in range(3):
                zero_matrix[i, k] = int(input('Введіть елементи матриці для одночасного транспонування: '))
                #реалізовано за допомогою перестановки стовпця і рядка місцями
        print(f'Ваша транспонована матриця:\n{zero_matrix}')
        break
    except ValueError:
        print("Введіть число!")
