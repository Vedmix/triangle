import matplotlib.pyplot as plt
from math import pi
from colorama import Fore, Back, Style, init
from functions_triangle import*

while True:

    init()

    print(Fore.CYAN)

    print('Введите координаты точек: ')

    x1, y1 = input('Точка А => ').split(';')
    x2, y2 = input('Точка B => ').split(';')
    x3, y3 = input('Точка C => ').split(';')

    x1, x2, x3 = float(x1), float(x2), float(x3)
    y1, y2, y3 = float(y1), float(y2), float(y3)

    if (x1 == x2 == x3) or (y1 == y2 == y3):
        print('Такого треугольника не существует!')
        continue

    AB = side(x1, y1, x2, y2)
    BC = side(x2, y2, x3, y3)
    AC = side(x1, y1, x3, y3)

    AF = lenght_median(AC, AB, BC)
    BD = lenght_median(AC, BC, AB)
    CE = lenght_median(AB, BC, AC)

    angle_BAC = angle(AC, AB, BC)
    angle_ABC = angle(AC, BC, AB)
    angle_BCA = angle(AB, BC, AC)

    # наименование точек
    fig, ax = plt.subplots()

    ax.text(x1 - 0.05, y1 - 0.05, 'A', style='italic', fontsize=15, color="purple")
    ax.text(x2 - 0.05, y2 + 0.05, 'B', style='italic', fontsize=15, color="purple")
    ax.text(x3 + 0.05, y3 - 0.05, 'C', style='italic', fontsize=15, color="purple")

    ax.text(((x2 + x3) / 2) + 0.05, ((y2 + y3) / 2), 'F', style='italic', fontsize=15, color="purple")
    ax.text(((x1 + x3) / 2), ((y1 + y3) / 2) - 0.05, 'D', style='italic', fontsize=15, color="purple")
    ax.text(((x1 + x2) / 2) - 0.05, ((y1 + y2) / 2), 'E', style='italic', fontsize=15, color="purple")

    # Медианы углов А, В, С
    mid_BC_x, mid_BC_y = ((x2 + x3) / 2), ((y2 + y3) / 2)
    median_A_x, median_A_y = [x1, mid_BC_x], [y1, mid_BC_y]

    mid_AC_x, mid_AC_y = ((x1 + x3) / 2), ((y1 + y3) / 2)
    median_B_x, median_B_y = [x2, mid_AC_x], [y2, mid_AC_y]

    mid_AB_x, mid_AB_y = ((x1 + x2) / 2), ((y1 + y2) / 2)
    median_C_x, median_C_y = [x3, mid_AB_x], [y3, mid_AB_y]

    print()

    print('Информация о треугольнике:')
    print()
    if (AB + BC > AC) and (BC + AC > AB) and (AB + AC > BC):
        if AB == BC == AC:
            print('Тип >> "Равносторонний треугольник"')
            print()
        elif (round(angle_BAC, 15) == round((pi / 2), 15)) or (round(angle_ABC, 15) == round((pi / 2), 15)) or (round(angle_BCA, 15) == round((pi / 2), 15)):
            print('Тип >> "Прямоугольный треугольник"')
            print()
        elif (round(angle_BAC, 15) < round((pi / 2), 15)) and (round(angle_ABC, 15) < round((pi / 2), 15)) and (round(angle_BCA, 15) < round((pi / 2), 15)):
            print('Тип >> "Остроугольный треугольник"')
            print()
        elif (round(angle_BAC, 15) > round((pi / 2), 15)) or (round(angle_ABC, 15) > round((pi / 2), 15)) or (round(angle_BCA, 15) > round((pi / 2), 15)):
            print('Тип >> "Тупоугольный треугольник"')
            print()
        elif (AB != BC == AC) or (AB == BC != AC) or (AB == AC != BC):
            print('Тип >> Равнобедренный треугольник')
        print('Площадь треугольника >> ' + str('%.2f' % square(AB, BC, AC)) + 'см')
        print()
        print('Периметр треугольника >> ' + str('%.2f' % perimeter_t(AB, BC, AC)) + 'см')

    else:
        print('Такого треугольника не существует!')
        continue

    print()

    print('Углы треугольника:')
    print('∠BAC >> ' + str('%.2f' % degrees(angle_BAC)) + '°')
    print('∠ABC >> ' + str('%.2f' % degrees(angle_ABC)) + '°')
    print('∠BCA >> ' + str('%.2f' % degrees(angle_BCA)) + '°')

    print()

    print('Стороны треугольника:')
    print('АВ >> ' + str('%.2f' % AB) + 'см')
    print('ВC >> ' + str('%.2f' % BC) + 'см')
    print('АC >> ' + str('%.2f' % AC) + 'см')

    print()

    print('Длины медиан:')
    print('AF >> ' + str('%.2f' % AF) + 'см')
    print('BD >> ' + str('%.2f' % BD) + 'см')
    print('CE >> ' + str('%.2f' % CE) + 'см')

    print()

    print('Уравнения сторон треугольника:')
    print('AB >> ' + equation_side(x1, y1, x2, y2))
    print('BC >> ' + equation_side(x2, y2, x3, y3))
    print('AC >> ' + equation_side(x1, y1, x3, y3))

    # print(''+str(r))
    x, y = [x1, x2, x3], [y1, y2, y3]
    x1, y1 = [x1, x3], [y1, y3]

    plt.plot(x, y, color='black')
    plt.plot(x1, y1, color='black')
    plt.plot(x, y, 'o')
    plt.plot(x1, y1, 'o')

    plt.plot(median_A_x, median_A_y, color='blue')
    plt.plot(median_A_x, median_A_y, 'o')

    plt.plot(median_B_x, median_B_y, color='blue')
    plt.plot(median_B_x, median_B_y, 'o')

    plt.plot(median_C_x, median_C_y, color='blue')
    plt.plot(median_C_x, median_C_y, 'o')

    ax.grid()
    plt.title('Ваш треугольник:')
    plt.show()

