import matplotlib.pyplot as plt
import math
from math import acos, degrees
from colorama import init
from colorama import Fore, Back, Style


def perimeter(side1, side2, side3,side4):
    return float((side1+side2+side3+side4))


def square(side1, side2, side3):
    p = perimeter(side1, side2, side3) / 2
    return (math.sqrt(p * (p - side1) * (p - side2) * (p - side3)))


def side(point_x_1, point_y_1, point_x_2, point_y_2):
    side = math.sqrt(((point_x_1 - point_x_2) ** 2) + ((point_y_1 - point_y_2) ** 2))
    return side


def lenght_median(side1, side2, side3):  # side3 вычитаем
    lenght_median = math.sqrt(2 * side1 ** 2 + 2 * side2 ** 2 - side3 ** 2) / 2
    return lenght_median


def angle(side1, side2, side3):  # side3 вычитаем
    angle = degrees(acos((side1 ** 2 + side2 ** 2 - side3 ** 2) / (2.0 * side1 * side2)))
    return angle


def equation_side(point_x_1, point_y_1, point_x_2, point_y_2):
    A = float(point_y_2 - point_y_1)
    B = float(point_x_1 - point_x_2)
    C = float(point_x_2 * point_y_1 - point_x_1 * point_y_2)
    return '(' + str(A) + ')' + 'x + ' + '(' + str(B) + ')' + 'y + ' + '(' + str(C) + ')' + ' = 0'


def line_coefficients(p1, p2):
    A = (p1[1] - p2[1])
    B = (p2[0] - p1[0])
    C = (p1[0] * p2[1] - p2[0] * p1[1])
    return A, B, -C


def intersection_x(L1, L2):
    D = L1[0] * L2[1] - L1[1] * L2[0]
    Dx = L1[2] * L2[1] - L1[1] * L2[2]
    if D != 0:
        x = Dx / D
        return x


def intersection_y(L1, L2):
    D = L1[0] * L2[1] - L1[1] * L2[0]
    Dy = L1[0] * L2[2] - L1[2] * L2[0]
    if D != 0:
        y = Dy / D
        return y

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

        AB = side(point_x_1=x1, point_y_1=y1, point_x_2=x2, point_y_2=y2)
        BC = side(point_x_1=x2, point_y_1=y2, point_x_2=x3, point_y_2=y3)
        AC = side(point_x_1=x1, point_y_1=y1, point_x_2=x3, point_y_2=y3)

        AF = lenght_median(side1=AC, side2=AB, side3=BC)  # math.sqrt(2*AC**2+2*AB**2-BC**2)/2#AC AB BC
        BD = lenght_median(side1=AC, side2=BC, side3=AB)  # math.sqrt(2*AC**2+2*BC**2-AB**2)/2#AC BC AB
        CE = lenght_median(side1=AB, side2=BC, side3=AC)  # math.sqrt(2*AB**2+2*BC**2-AC**2)/2#AB BC AC

        angle_BAC = angle(side1=AC, side2=AB, side3=BC)  # degrees(acos((AC**2+AB**2-BC**2)/(2.0 * AB * AC)))
        angle_ABC = angle(side1=AC, side2=BC, side3=AB)  # degrees(acos((AC**2+BC**2-AB**2)/(2.0 * AC * BC)))
        angle_BCA = angle(side1=AB, side2=BC, side3=AC)  # degrees(acos((AB**2+BC**2-AC**2)/(2.0 * AB * BC)))

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

        print(Fore.GREEN)

        print('Информация о треугольнике:')
        if (AB + BC > AC) and (BC + AC > AB) and (AB + AC > BC):
            if AB == BC == AC:
                print('Тип >> "Равносторонний треугольник"')
            elif (angle_BAC == 90) or (angle_ABC == 90) or (angle_BCA == 90):
                print('Тип >> "Прямоугольный треугольник"')
            elif (angle_BAC < 90) and (angle_ABC < 90) and (angle_BCA < 90):
                print('Тип >> "Остроугольный треугольник"')
            elif (angle_BAC > 90) or (angle_ABC > 90) or (angle_BCA > 90):
                print('Тип >> "Тупоугольный треугольник"')
            elif (AB != BC == AC) or (AB == BC != AC) or (AB == AC != BC):
                print('Тип >> Равнобедренный треугольник')
            print('Площадь треугольника >> ' + str('%.2f' % square(side1=AB, side2=BC, side3=AC)) + 'см')
            print('Периметр треугольника >> ' + str('%.2f' % perimeter(side1=AB, side2=BC, side3=AC)) + 'см')

        else:
            print('Такого треугольника не существует!')
            continue

        print(Fore.BLUE)

        print('Углы треугольника:')
        print('∠BAC >> ' + str('%.2f' % angle_BAC) + '°')
        print('∠ABC >> ' + str('%.2f' % angle_ABC) + '°')
        print('∠BCA >> ' + str('%.2f' % angle_BCA) + '°')

        print(Fore.MAGENTA)

        print('Стороны треугольника:')
        print('АВ >> ' + str('%.2f' % AB) + 'см')
        print('ВC >> ' + str('%.2f' % BC) + 'см')
        print('АC >> ' + str('%.2f' % AC) + 'см')

        print(Fore.MAGENTA)

        print('Длины медиан:')
        print('AF >> ' + str('%.2f' % AF) + 'см')
        print('BD >> ' + str('%.2f' % BD) + 'см')
        print('CE >> ' + str('%.2f' % CE) + 'см')

        print(Fore.MAGENTA)

        print('Уравнения сторон треугольника:')
        print('AB >> ' + equation_side(point_x_1=x1, point_y_1=y1, point_x_2=x2, point_y_2=y2))
        print('BC >> ' + equation_side(point_x_1=x2, point_y_1=y2, point_x_2=x3, point_y_2=y3))
        print('AC >> ' + equation_side(point_x_1=x1, point_y_1=y1, point_x_2=x3, point_y_2=y3))

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

        AB = side(point_x_1=x1, point_y_1=y1, point_x_2=x2, point_y_2=y2)
        BC = side(point_x_1=x2, point_y_1=y2, point_x_2=x3, point_y_2=y3)
        CD = side(point_x_1=x3, point_y_1=y3, point_x_2=x4, point_y_2=y4)
        AD = side(point_x_1=x1, point_y_1=y1, point_x_2=x4, point_y_2=y4)

        AC = side(point_x_1=x2, point_y_1=y2, point_x_2=x4, point_y_2=x4)
        BD = side(point_x_1=x1, point_y_1=y1, point_x_2=x3, point_y_2=x3)

        AC1 = line_coefficients([x1, y1], [x3, y3])
        BD1 = line_coefficients([x2, y2], [x4, y4])

        O_X = intersection_x(AC1, BD1)
        O_Y = intersection_y(AC1, BD1)

        AO = side(point_x_1=x1, point_y_1=y1, point_x_2=O_X, point_y_2=O_Y)
        BO = side(point_x_1=x2, point_y_1=y2, point_x_2=O_X, point_y_2=O_Y)
        CO = side(point_x_1=x3, point_y_1=y3, point_x_2=O_X, point_y_2=O_Y)
        DO = side(point_x_1=x3, point_y_1=y3, point_x_2=O_X, point_y_2=O_Y)

        A = [x1, y1]
        B = [x2, y2]
        C = [x3, y3]
        D = [x4, y4]

        AB1 = [B[0] - A[0], B[1] - A[1]]
        BC1 = [C[0] - B[0], C[1] - B[1]]
        CD1 = [D[0] - C[0], D[1] - C[1]]
        DA1 = [A[0] - D[0], A[1] - D[1]]

        ABC = degrees(acos((AB1[0] * BC1[0] + AB1[1] * BC1[1]) / (math.sqrt(AB1[0] ** 2 + AB1[1] ** 2) * math.sqrt(BC1[0] ** 2 + BC1[1] ** 2))))
        BCD = degrees(acos((BC1[0] * CD1[0] + BC1[1] * CD1[1]) / (math.sqrt(BC1[0] ** 2 + BC1[1] ** 2) * math.sqrt(CD1[0] ** 2 + CD1[1] ** 2))))
        CDA = degrees(acos((CD1[0] * DA1[0] + CD1[1] * DA1[1]) / (math.sqrt(CD1[0] ** 2 + CD1[1] ** 2) * math.sqrt(DA1[0] ** 2 + DA1[1] ** 2))))
        DAB = degrees(acos((DA1[0] * AB1[0] + DA1[1] * AB1[1]) / (math.sqrt(DA1[0] ** 2 + DA1[1] ** 2) * math.sqrt(AB1[0] ** 2 + AB1[1] ** 2))))

        # BOA=square(side1=AB, side2=BO, side3=AO)
        # BCO=square(side1=BO, side2=BC, side3=CO)
        # COD=square(side1=CO, side2=CD, side3=DO)
        # DOA=square(side1=DO, side2=AO, side3=AD)

        print('информация о четырехугольнике:')
        print()

        if (round(ABC, 2) + round(DAB, 2) == 180):
            II_AB_CD = True
        else:
            II_AB_CD = False

        if (round(BCD, 2) + round(CDA, 2) == 180):
            II_BC_AD = True
        else:
            II_BC_AD = False

        angle_a = angle(BO, AO, AB)
        h=side(x2,y2,x2,x1)

        if (round(DAB, 2) == round(ABC, 2) == round(BCD, 2) == round(CDA, 2) == 90.00):
            if (AB == BC == CD == AD):
                print('Тип >> "Квадрат"')
                print('Площадь четырехтреугольника >> ' + str('%.2f' %(AB ** 2)) + 'см')
            elif ((AB == CD) and (BC == AD)):
                print('Тип >> "Прямоугольник"')
                print('Площадь четырехтреугольника >> ' + str('%.2f' %(AB * BC)) + 'см')
        elif ((AB ** 2 == AO ** 2 + BO ** 2) == (BC ** 2 == CO ** 2 + BO ** 2) == (CD ** 2 == CO ** 2 + DO ** 2) == (
                AD ** 2 == DO ** 2 + AO ** 2)):
            if (AB == BC == CD == AD):
                print('Тип >> "Ромб"')
                print('Площадь четырехтреугольника >> ' + str('%.2f' %(((AC * BD) / 2))) + 'см')
            elif (((AB == BC) and (CD == AD)) or ((BC == CD) and (AB == AD))):
                print('Тип >> "Дельтоид"')
                print('Площадь четырехтреугольника >> ' + str('%.2f' %(((AC * BD) / 2))) + 'см')
        elif ((AB == CD) and (BC == AD)) and ((round(DAB, 2) == round(BCD, 2)) and (round(ABC, 2) == round(CDA, 2))) and ((II_AB_CD == True) and (II_BC_AD == True)):
            print('Тип >> "Параллелограмм"')
            print('Площадь четырехтреугольника >> ' + str('%.2f' %((math.sin(CDA) * (AB * AD)))) + 'см')
        elif (II_AB_CD == II_BC_AD == False) and (AB != BC != CD != AD):
            print('Тип >> "Произвольный четырехугольник"')

        if ((II_BC_AD == True) or (II_AB_CD == True)):
            if ((AB == CD) or (BC == AD)):
                print('Тип >> "Равнобедренная трапеция"')
                print('Площадь четырехтреугольника >> '+str('%.2f' %((((BC+AD)/2)*h)))+ 'см')
            elif (round(DAB, 2) == round(ABC, 2) == 90.00) or (round(BCD, 2) == round(CDA, 2) == 90.00):
                print('Тип >> "Прямоугольная трапеция"')
                print('Площадь четырехтреугольника >> ' + str('%.2f' %((((BC + AD) / 2) * h))) + 'см')
            else:
                print('Тип >> "Произвольная трапеция"')
                print('Площадь четырехтреугольника >> ' + str('%.2f' %((((BC + AD) / 2) * h))) + 'см')
                
        print()
        print('Периметр четырехугольника >> ' + str('%.2f' %(perimeter(AB, BC, CD, AD))) + 'см')
        print()
        print('Стороны четырехугольника:')
        print()
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
