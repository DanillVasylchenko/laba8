'''
Задача полягає у вивченні і реалізації алгоритмів пошуку для даних, підготовлених
за допомогою функції моделювання випадкових чисел і текстів, підготовлених
самостійно.
Для кожного алгоритму необхідно підготувати тести, що підтверджують
працездатність програми. Для всіх алгоритмів пошуку повинні бути приведені лістинги
програм пошуку та лістинги результатів (номера позиції в вихідному масиві, починаючи
з якого розташований елемент або фрагмент пошуку; кількості порівнянь по кожному
алгоритму пошуку).
Найпростіші алгоритми пошуку:
 лінійний пошук;
 бінарний пошук;
 прямий пошук підрядка.

Васильченко Даниїл Назарович 122 А
'''
import numpy as np


def my_input(text_def): #самостійне введеня
    while True:
        try:
            input_num = int(input(text_def))
            break
        except ValueError:
            print('Введіть число!')
    return input_num


def line_search(a_def, x_def): #лінійне введення
    print("array :")
    print(a_def)
    i_def = 0
    g_def = len(a_def)
    counter_def = 0
    while i_def < g_def and a_def[i_def] != x_def:
        counter_def += 2
        i_def += 1
    if i_def == g_def:
        print('Елемент', x_def, 'Не знайдено.')
        print('Число порівнянь: ', counter_def)
    else:
        print('Елемент', x_def, 'Знайдено на позиції', i_def)
        print('Число порівнянь: ', counter_def)


def binary_search(a_def, x_def): #бінарний пошук
    a_def.sort() #сортування масиву
    g_def = len(a_def)
    print("Масив: \n", a_def)
    i = 0
    L = 0
    R = g_def - 1
    flag = True
    counter_def = 0
    while L <= R and flag:
        i += 1
        K = (L + R) // 2
        if a_def[K] == x_def:
            counter_def += 2
            print('Елемент', x_def, 'Було знайдено на позиції', K)
            print('Число порівнянь:', counter_def)
            flag = False
        elif a_def[K] < x_def:
            counter_def += 3
            L = K + 1
        elif a_def[K] > x_def:
            counter_def += 4
            R = K - 1
    if flag:
        print('Елемент', x_def, 'Не знайдено.')
        print('Число порівнянь:', counter_def)


def patter_search(text_def, pattern_def): #пошук підрядка
    i = -1
    j = 0
    counter_def = 0
    while (j < len(pattern_def)) and i < (len(text_def) - len(pattern_def)):
        counter_def += 2
        j = 0
        i += 1
        while j < len(pattern_def) and pattern_def[j] == text_def[i + j]:
            counter_def += 2
            j += 1
    if j == len(pattern_def):
        print('Pattern', pattern_def, 'Знайдено в позиції', i)
    else:
        print('Елемент', pattern_def, 'Не знайдено, мені дуже шкода...')
    print('Число порівнянь:', counter_def)


while True:
    print("Лінійний пошук:\n")
    choice = input("Введіть щось, якщо хочете самостійно ввести дані або натисніть Enter і програма обере випадкові значення: ")
    if len(choice) > 0:
        massive_length = my_input('Довжина масиву: ')
        searched_el = my_input('Шуканий елемент: ')
        zero_matrix = np.zeros(massive_length, dtype=int)
        print("Введення масиву:")
        for i in range(massive_length):
            zero_matrix[i] = my_input("Введіть число типу int: ")
        line_search(zero_matrix, searched_el)  #виклик функції
    else:
        # Шуканого елементу немає в масиві
        massive_length = 20  # Довжина масиву
        searched_el = 15  # Шуканий елемент
        last = 15
        zero_matrix = np.random.randint(0, last, massive_length)  # (start, stop, len) генерація випадкового масиву
        line_search(zero_matrix, searched_el)  # Виклик функції лінійного пошуку
        print()
        # Шуканий елемент є в масиві
        massive_length = 20  # Довжина масиву
        searched_el = 2  # Шуканий елемент
        last = 10
        zero_matrix = np.random.randint(0, last, massive_length)  # (start, stop, len) генерація випадкового масиву
        zero_matrix[-1] = searched_el
        line_search(zero_matrix, searched_el)  # виклик функції

    print("Бінарний пошук:\n")
    choice = input("Введіть щось, якщо хочете самостійно ввести дані або натисніть Enter і програма обере випадкові значення: ")
    if len(choice) > 0:
        massive_length = my_input('Довжина масиву: ')  # довжина масиву
        searched_el = my_input('Шуканий елемент: ')  # шуканий елемент
        zero_matrix = np.zeros(massive_length, dtype=int)
        print("Введеня масиву: ")
        for i in range(massive_length):
            zero_matrix[i] = my_input("Введіть число типу int: ")
        binary_search(zero_matrix, searched_el)# виклик функції бінарного пошуку

    else:
        massive_length = 20
        searched_el = 12
        last = 10
        zero_matrix = np.random.randint(0, last, massive_length)  # (start, stop, len) генерация рандомного массива
        binary_search(zero_matrix, searched_el)# виклик функції бінарного пошуку
        print()
        massive_length = 20
        searched_el = 2
        last = 10
        zero_matrix = np.random.randint(0, last, massive_length)  # (start, stop, len) генерация рандомного массива
        binary_search(zero_matrix, searched_el)# виклик функції бінарного пошуку



    print("Прямий пошук підрядка:\n")
    choice = input("Введіть щось, якщо хочете самостійно ввести дані або натисніть Enter і програма обере випадкові значення: ")
    if len(choice) > 0:
        string = input("Введіть рядок")
        pattern = input("Введите підрядок, який можна знайти")
        patter_search(string, pattern)
    else:
        # Шуканий підрядок є в рядку
        string = "зарахуйте будь ваша ласка"
        pattern = "ваша"
        patter_search(string, pattern)
        print()
        # Шуканий підрядок відсутній в рядок
        pattern = "не"
        patter_search(string, pattern)
    if input('Натисніть "Enter" для перезапуску і введіть щось, якщо воно вам не треба, Наталія Артурівна: ') == '':
        continue
    break
