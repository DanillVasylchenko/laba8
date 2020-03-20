''' 2. Для даних, наведених в задачі 14, скласти програму, яка обчислювала б і виводила
 на екран:
 • середні питомі ваги напівпровідників, провідників та ізоляторів;
 • найменування речовин різної провідності, що мають мінімальну і максимальну
 питому вагу
 14. Відомості про речовину складаються з його назви, питомої ваги і провідності
 (провідник, напівпровідник, ізолятор).
 Васильченко Даниїл Назарович 1 курс група 122А
'''

while True:
    name_l = [input('Введіть назву речовини') for i in range(int(input('Скільки речовин ви хочете ввести? ')))]
    specific_weight_l = [55, 44]
    conductivity_l = ['провідник', 'напівпровідник']
    types_of_conductivity = ['провідник', 'напівпровідник', 'ізолятор']
    specific_weight = dict(zip(name_l, specific_weight_l))
    conductivity = dict(zip(name_l, conductivity_l))
    mean_specific_weight_of_0 = 0
    mean_specific_weight_of_1 = 0
    mean_specific_weight_of_2 = 0
    max_of_specific_weight = []
    min_of_specific_weight = []
    for i in specific_weight:
        if conductivity[i] == types_of_conductivity[0]:
            mean_specific_weight_of_0 += specific_weight[i]
        elif conductivity[i] == types_of_conductivity[1]:
            mean_specific_weight_of_1 += specific_weight[i]
        elif conductivity[i] == types_of_conductivity[2]:
            mean_specific_weight_of_2 += specific_weight[i]
        if specific_weight[i] == max(specific_weight_l):
            max_of_specific_weight.append(i)
        if specific_weight[i] == min(specific_weight_l):
            min_of_specific_weight.append(i)
    print('Середня питома вага провідників:', mean_specific_weight_of_0)
    print('Середня питома вага напівпровідників:', mean_specific_weight_of_1)
    print('Середня питома вага ізоляторів:', mean_specific_weight_of_2)
    print('Найменування речовин різної провідності, що мають  максимальну питому вагу:', max_of_specific_weight)
    print('Найменування речовин різної провідності, що мають  мінімальну питому вагу:', min_of_specific_weight)

    if input('Натисніть "Enter" для перезапуску: ') == '':
        continue
    break
