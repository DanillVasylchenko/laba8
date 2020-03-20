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


def my_input(text_def):  # самостійне введення даних
    while True:
        try:
            input_num = int(input(text_def))
            break
        except ValueError:
            print('only digit')
    return input_num


def line_search(last_def, g_def, x_def, tr_def=False):  # лінійний пошук
    a_def = np.random.randint(0, last_def, g_def)
    if tr_def:
        a_def[g_def // 2] = x_def
    print("random number array :")
    print(a_def)
    i_def = 0
    while i_def < g_def:
        if a_def[i_def] == x_def:
            i_def += 1
            break
        i_def += 1
    if i_def == g_def:
        print('Item', x_def, 'not found.')
        print('number of comparisons:', i_def)
    else:
        print('Item', x_def, 'first found in position', i_def)
        print('number of comparisons:', i_def)




def binary_search(last_def, g_def, x_def, tr_def=False):  # бінарний пошук
    a_def = np.random.randint(0, last_def, g_def)
    if tr_def:
        a_def[g_def // 2] = x_def
    a_def.sort()
    print("random number array :")
    print(a_def)
    i = 0
    L = 0
    R = g_def - 1
    flag = True
    while L <= R and flag:
        i += 1
        K = (L + R) // 2
        if a_def[K] == x_def:
            print('Item', x_def, 'first found in position', K)
            print('number of comparisons:', i)
            flag = False
        elif a_def[K] < x_def:
            L = K + 1
        elif a_def[K] > x_def:
            R = K - 1
    if flag:
        print('Item', x_def, 'not found.')
        print('number of comparisons:', i)


def pattern_search(text_def, pattern_def):  # пошук підрядка
    i = -1
    j = 0
    count_def = 0
    while (j < len(pattern_def)) and i < (len(text_def) - len(pattern_def)):
        j = 0
        i += 1
        while j < len(pattern_def) and pattern_def[j] == text_def[i + j]:
            j += 1
            count_def += 1
    if j == len(pattern_def):
        print('Pattern', pattern_def, 'first found in position', i)
    else:
        print('Item', pattern_def, 'not found.')
    print('number of comparisons:', count_def)


while True:
    print("Лінійний пошук:\n")
    # # g = my_input('count of elements: ')
    # # x = my_input('required element (int 0-100): ')

    g = 20
    x = 15
    last = 15
    line_search(last, g, x)
    print()
    g = 20
    x = 2
    last = 10
    line_search(last, g, x, True)

    print("Бінарний пошук:\n")
    g = 20
    x = 12
    last = 10
    binary_search(last, g, x, False)
    print()
    g = 20
    x = 2
    last = 10
    binary_search(last, g, x, True)

    print("Прямий пошук підрядка:\n")
    text = "помився побрився ліг спати і вкрився"
    pattern = "ліг"
    pattern_search(text, pattern)
    print()
    pattern = "спатки"
    pattern_search(text, pattern)
    if input('Нажмите "Enter" (введите пустую строку (\'\')) для перезапуска: ') == '':
        continue
    break
