import matplotlib.pyplot as plt
from math import pi
from colorama import Fore, init
from functions_triangle import*

while True:

    init()

    print(Fore.CYAN)

    print('Введите координаты точек: ')

    x1, y1 = list(map(float,input('Точка А => ').split(';')))
    x2, y2 = list(map(float,input('Точка B => ').split(';')))
    x3, y3 = list(map(float,input('Точка C => ').split(';')))

    if [x1, y1] == [x2, y2] or [x1, y1] == [x3, y3] or [x2, y2] == [x3, y3]:
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

            print('Тип >> "Равносторонний треугольник"'); type=1
            print()

        elif (round(angle_BAC, 15) == round((pi / 2), 15)) or (round(angle_ABC, 15) == round((pi / 2), 15)) or (round(angle_BCA, 15) == round((pi / 2), 15)):

            if (AB != BC == AC) or (AB == BC != AC) or (AB == AC != BC):

                print('Тип >> "Прямоугольный треугольник" с равнобедренными боковыми сторонами'); type = 2
                print()

            else:

                print('Тип >> "Прямоугольный треугольник"'); type = 2
                print()

        elif (round(angle_BAC, 15) < round((pi / 2), 15)) and (round(angle_ABC, 15) < round((pi / 2), 15)) and (round(angle_BCA, 15) < round((pi / 2), 15)):

            if (AB != BC == AC) or (AB == BC != AC) or (AB == AC != BC):

                print('Тип >> "Остроугольный треугольник" с равнобедренными боковыми сторонами'); type=3
                print()

            else:

                print('Тип >> "Остроугольный треугольник"'); type = 3
                print()

        elif (round(angle_BAC, 15) > round((pi / 2), 15)) or (round(angle_ABC, 15) > round((pi / 2), 15)) or (round(angle_BCA, 15) > round((pi / 2), 15)):

            if (AB != BC == AC) or (AB == BC != AC) or (AB == AC != BC):

                print('Тип >> "Тупоугольный треугольник" с равнобедренными боковыми сторонами'); type=4
                print()

            else:

                print('Тип >> "Тупоугольный треугольник"'); type = 4
                print()

        print(f'Площадь треугольника >> {"%.2f " %square(AB, BC, AC)}')
        print()
        print(f'Периметр треугольника >> {"%.2f" % perimeter_t(AB, BC, AC)}')

    else:

        print('Такого треугольника не существует!')
        continue

    match type:
        case 1:
            xh,yh = [x2, (x1+x3)/2], [y2, (y1+y3)/2]
            a = side(x1, y1, x3, y3)
            h = ((2 * square(AB, BC, AC)) / a)
        case 2:
            if (x1 == x2) and (y1 != y2):
                xh,yh = [x1, x2], [y1, y2]
                if (y1 == y3):
                    a = side(x1, y1, x3, y3)
                if (y2 == y3):
                    a = side(x2, y2, x3, y3)
            elif (x2 == x3) and (y2 != y3):
                xh,yh = [x2, x3],[y2, y3]
                if (y1 == y3):
                    a = side(x1, y1, x3, y3)
                if (y1 == y2):
                    a = side(x1, y1, x2, y2)
            else:
                xh, yh = [x2, x2], [y2, y1]
                a = side(x1, y1, x3, y3)
            h = ((2 * square(AB, BC, AC)) / a)
        case 3:
            if y1 == y3:
                xh, yh = [x2, x2], [y2, y1]
                a = side(x1, y1, x3, y3)
                h = ((2 * square(AB, BC, AC)) / a)
            elif y2 == y3:
                xh, yh = [x1, x1], [y1, y2]
                a = side(x2, y2, x3, y3)
                h = ((2 * square(AB, BC, AC)) / a)
            elif y1 == y2:
                xh, yh = [x3, x3], [y3, y2]
                a = side(x2, y2, x1, y1)
                h = ((2 * square(AB, BC, AC)) / a)
            else:
                h = 0
        case 4:
            if y1 == y3:
                xh, yh = [x2, x2], [y2, y1]
                a = side(x1, y1, x3, y3)
                h = ((2 * square(AB, BC, AC)) / a)
            elif y2 == y3:
                xh, yh = [x1, x1], [y1, y2]
                a = side(x2, y2, x3, y3)
                h = ((2 * square(AB, BC, AC)) / a)
            elif y1 == y2:
                xh, yh = [x3, x3], [y3, y2]
                a = side(x2, y2, x1, y1)
                h = ((2 * square(AB, BC, AC)) / a)
            else:
                h = 0

    print()

    print('Углы треугольника:')
    print(f'∠BAC >> {"%.2f" % degrees(angle_BAC)}°')
    print(f'∠ABC >> {"%.2f" % degrees(angle_ABC)}°')
    print(f'∠BCA >> {"%.2f" % degrees(angle_BCA)}°')

    print()

    print('Стороны треугольника:')
    print(f'АВ >> {"%.2f" % AB}')
    print(f'ВC >> {"%.2f" % BC}')
    print(f'АC >> {"%.2f" % AC}')
    
    print()

    print('Длины медиан:')
    print(f'AF >> {"%.2f" % AF}')
    print(f'BD >> {"%.2f" % BD}')
    print(f'CE >> {"%.2f" % CE}')

    print()

    print('Длина высоты:')
    print(f'h >> {"%.2f" %h}')

    print()

    print('Уравнения сторон треугольника:')
    print(f'AB >> {equationYKB(x1, y1, x2, y2)}')
    print(f'BC >> {equationYKB(x2, y2, x3, y3)}')
    print(f'AC >> {equationYKB(x1, y1, x3, y3)}')

    x, y = [x1, x2, x3], [y1, y2, y3]
    x1, y1 = [x1, x3], [y1, y3]

    plt.plot(x, y, color='black', label='сторона')
    plt.plot(x, y, 'o')

    plt.plot(x1, y1, color='black', label='сторона')
    plt.plot(x1, y1, 'o')

    plt.plot(median_A_x, median_A_y, color='blue', label='медиана')
    plt.plot(median_A_x, median_A_y, 'o')

    plt.plot(median_B_x, median_B_y, color='blue', label='медиана')
    plt.plot(median_B_x, median_B_y, 'o')

    plt.plot(median_C_x, median_C_y, color='blue', label='медиана')
    plt.plot(median_C_x, median_C_y, 'o')

    plt.plot(xh, yh, color='red', label='высота')
    plt.plot(xh, yh, 'o')

    ax.grid()
    plt.title('Ваш треугольник:')
    plt.legend()
    plt.show()