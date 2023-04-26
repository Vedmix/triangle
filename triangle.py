import matplotlib.pyplot as plt
from math import acos, degrees, sqrt, sin
from colorama import Fore, Back, Style, init
from functions_triangle import*

while True:

    init()

    print(Fore.CYAN)

    count_points = int(input('Введите количество точек (3-4) => '))

    if count_points == 3:
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
    elif count_points == 4:
        print('Введите координаты точек: ')

        x1, y1 = input('Точка А => ').split(';')
        x2, y2 = input('Точка B => ').split(';')
        x3, y3 = input('Точка C => ').split(';')
        x4, y4 = input('Точка D => ').split(';')

        x1, x2, x3, x4 = float(x1), float(x2), float(x3), float(x4)
        y1, y2, y3, y4 = float(y1), float(y2), float(y3), float(y4)

        if (x1 == x2 == x3==x4) or (y1 == y2 == y3==y4):
            print('Такого четырехугольника не существует!')
            continue

        AB = side(x1, y1, x2, y2)
        BC = side(x2, y2, x3, y3)
        CD = side(x3, y3, x4, y4)
        AD = side(x1, y1, x4, y4)

        AC = side(x2, y2, x4, x4)
        BD = side(x1, y1, x3, x3)

        AC1 = line_coefficients([x1, y1], [x3, y3])
        BD1 = line_coefficients([x2, y2], [x4, y4])

        O_X = intersection_x(AC1, BD1)
        O_Y = intersection_y(AC1, BD1)

        # Середины сторон
        E=[((x1+x2)/2),((y1+y2)/2)]
        G=[((x2+x3)/2),((y2+y3)/2)]
        F=[((x3+x4)/2),((y3+y4)/2)]
        H=[((x1+x4)/2),((y1+y4)/2)]

        # Средние линии
        EF = line_coefficients([E[0], E[1]], [F[0], F[1]])
        GH = line_coefficients([G[0], G[1]], [H[0], H[1]])

        # Точка пересечения средних линий
        Z_X = intersection_x(EF,GH)
        Z_Y = intersection_y(EF, GH)

        AO = side(x1, y1, O_X, O_Y)
        BO = side(x2, y2, O_X, O_Y)
        CO = side(x3, y3, O_X, O_Y)
        DO = side(x3, y3, O_X, O_Y)

        A = [x1, y1]
        B = [x2, y2]
        C = [x3, y3]
        D = [x4, y4]

        AB1 = [B[0] - A[0], B[1] - A[1]]
        BC1 = [C[0] - B[0], C[1] - B[1]]
        CD1 = [D[0] - C[0], D[1] - C[1]]
        DA1 = [A[0] - D[0], A[1] - D[1]]

        ABC = degrees(acos((AB1[0] * BC1[0] + AB1[1] * BC1[1]) / (sqrt(AB1[0] ** 2 + AB1[1] ** 2) * sqrt(BC1[0] ** 2 + BC1[1] ** 2))))
        BCD = degrees(acos((BC1[0] * CD1[0] + BC1[1] * CD1[1]) / (sqrt(BC1[0] ** 2 + BC1[1] ** 2) * sqrt(CD1[0] ** 2 + CD1[1] ** 2))))
        CDA = degrees(acos((CD1[0] * DA1[0] + CD1[1] * DA1[1]) / (sqrt(CD1[0] ** 2 + CD1[1] ** 2) * sqrt(DA1[0] ** 2 + DA1[1] ** 2))))
        DAB = degrees(acos((DA1[0] * AB1[0] + DA1[1] * AB1[1]) / (sqrt(DA1[0] ** 2 + DA1[1] ** 2) * sqrt(AB1[0] ** 2 + AB1[1] ** 2))))

        print('Информация о четырехугольнике:')
        print()

        if (round(ABC, 2) + round(DAB, 2) == 180):
            II_AB_CD = True
        else:
            II_AB_CD = False

        if (round(BCD, 2) + round(CDA, 2) == 180):
            II_BC_AD = True
        else:
            II_BC_AD = False

        angle_a=angle(AO,DO,AD)
        h=side(x2,y2,x2,y1)

        while True:
            if (round(DAB, 2) == round(ABC, 2) == round(BCD, 2) == round(CDA, 2) == 90.00):
                if (AB == BC == CD == AD):

                    print('Тип >> "Квадрат"')
                    print()
                    print('Площадь четырехтреугольника >> ' + str('%.2f' % (AB ** 2)) + 'см')

                    break

                elif ((AB == CD) and (BC == AD)):

                    print('Тип >> "Прямоугольник"')
                    print()
                    print('Площадь четырехтреугольника >> ' + str('%.2f' % (AB * BC)) + 'см')

                    break

            elif ((AB ** 2 == AO ** 2 + BO ** 2) == (BC ** 2 == CO ** 2 + BO ** 2) == (CD ** 2 == CO ** 2 + DO ** 2) == (AD ** 2 == DO ** 2 + AO ** 2)):
                if (AB == BC == CD == AD):

                    print('Тип >> "Ромб"')
                    print()
                    print('Площадь четырехтреугольника >> ' + str('%.2f' % (((AC * BD) / 2))) + 'см')

                    break

                elif (((AB == BC) and (CD == AD)) or ((BC == CD) and (AB == AD))):

                    print('Тип >> "Дельтоид"')
                    print()
                    print('Площадь четырехтреугольника >> ' + str('%.2f' % (((AC * BD) / 2))) + 'см')

                    break

            elif ((AB == CD) and (BC == AD)) and ((round(DAB, 2) == round(BCD, 2)) and (round(ABC, 2) == round(CDA, 2))) and ((II_AB_CD == True) and (II_BC_AD == True)):

                print('Тип >> "Параллелограмм"')
                print()
                print('Площадь четырехтреугольника >> ' + str('%.2f' % ((sin(CDA) * (AB * AD)))) + 'см')

                break

            if (AB!=BC!=CD!=AD):

                print('Тип >> "Произвольный четырехугольник"')
                print()
                print('Площадь четырехтреугольника >> ' + str('%.2f' % ((AC*BD*sin(angle_a))/2)) + 'см')

                break

            if ((II_BC_AD == True) or (II_AB_CD == True)):

                if ((AB == CD) or (BC == AD)):
                    print('Тип >> "Равнобедренная трапеция"')
                    print()
                    print('Площадь четырехтреугольника >> ' + str('%.2f' % ((((BC + AD) / 2) * h))) + 'см')

                    break

                elif (round(DAB, 2) == round(ABC, 2) == 90.00) or (round(BCD, 2) == round(CDA, 2) == 90.00):
                    print('Тип >> "Прямоугольная трапеция"')
                    print()
                    print('Площадь четырехтреугольника >> ' + str('%.2f' % ((((BC + AD) / 2) * h))) + 'см')

                    break

                else:
                    print('Тип >> "Произвольная трапеция"')
                    print()
                    print('Площадь четырехтреугольника >> ' + str('%.2f' % ((((BC + AD) / 2) * h))) + 'см')

                    break
        print(angle_a)
        print()

        print('Периметр четырехугольника >> ' + str('%.2f' %(perimeter_e(AB, BC, CD, AD))) + 'см')

        print()

        print('Стороны четырехугольника:')
        print('АВ >> ' + str('%.2f' % AB) + 'см')
        print('BC >> ' + str('%.2f' % BC) + 'см')
        print('CD >> ' + str('%.2f' % CD) + 'см')
        print('АD >> ' + str('%.2f' % AD) + 'см')

        print()

        print('Диагонали четырехугольника:')
        print('АC >> ' + str('%.2f' % AC) + 'см')
        print('BD >> ' + str('%.2f' % BD) + 'см')

        print()

        print('Углы четырехугольника:')
        print('∠ABC >> ' + str('%.2f' % BCD) + '°')
        print('∠BCD >> ' + str('%.2f' % ABC) + '°')
        print('∠CDA >> ' + str('%.2f' % DAB) + '°')
        print('∠DAB >> ' + str('%.2f' % CDA) + '°')

        print()

        print('Уравнения сторон четырехугольника')
        print('AB >> '+equation_side(x1,y1,x2,y2))
        print('BC >> '+equation_side(x2,y2,x3,y3))
        print('CD >> '+equation_side(x3,y3,x4,y4))
        print('AD >> '+equation_side(x1,y1,x4,y4))

        x, y = [x1, x2, x3, x4], [y1, y2, y3, y4]
        x11, y11 = [x1, x4], [y1, y4]
        x111, y111= [x1,x3], [y1,y3]
        x1111, y1111= [x2,x4], [y2,y4]

        plt.plot(x, y, color='black')
        plt.plot(x11, y11, color='black')
        plt.plot(x111, y111, color='blue')
        plt.plot(x1111, y1111, color='blue')

        plt.plot(x, y, 'o')
        plt.plot(x11, y11, 'o')
        plt.plot(x111, y111, 'o')
        plt.plot(x1111, y1111, 'o')

        plt.title('Ваш четырехугольник:')
        plt.show()

        break
    else:
        continue
