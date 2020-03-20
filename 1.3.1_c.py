'''
виконайте добуток двох квадратних матриць 3*3, врахуйте розмірність.
Результати множення елементів занесіть до нової матриці та виведіть її на екран;
Васильченко Даниїл Назарович 122 А
'''
import numpy as np

zero_matrix = np.zeros((3, 3), dtype=int)


def matrix_multiplication(zero_matrix):
    for i in range(3):
        for k in range(3):
            zero_matrix[i][k] = int(input(f'Введіть елемент [{i + 1},{k + 1}] 1-ї матриці:'))
    return zero_matrix


while True:
    try:
        matrix_1 = matrix_multiplication(zero_matrix)
        matrix_2 = matrix_multiplication(zero_matrix)
        break
    except ValueError:
        print("Введіть число!")

print(f'Ваша 1-а матриця:\n{matrix_1}')
print(f'Ваша 2-а матриця:\n{matrix_2}')

column = 0
new_matrix = np.zeros((3, 3), dtype=int)
for i in range(3):
    for k in range(3):
        for stop in range(3):
            new_matrix[i, k] += (matrix_1[i, stop] * matrix_2[stop, column])
        column += 1
    column = 0
print(f'Результат множення матриць:\n{new_matrix}')
