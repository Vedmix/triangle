import matplotlib.pyplot as plt
import math
from math import acos, degrees
from colorama import init
from colorama import Fore, Back, Style


def perimeter(AB, BC, AC):
     return float((AB+BC+AC))
def square(AB, BC, AC):
     p=perimeter(AB, BC, AC)/2
     return (math.sqrt(p*(p-AB)*(p-BC)*(p-AC)))
def side(point_x_1,point_y_1,point_x_2,point_y_2):
    side=math.sqrt(((point_x_1 - point_x_2) ** 2) + ((point_y_1 - point_y_2) ** 2))
    return side
def lenght_median(side1,side2,side3): #side3 вычитаем
    lenght_median=math.sqrt(2*side1**2+2*side2**2-side3**2)/2
    return lenght_median
def angle(side1,side2,side3): #side3 вычитаем
    angle = degrees(acos((side1 ** 2 + side2 ** 2 - side3 ** 2) / (2.0 * side1 * side2)))
    return angle
def equation_side(point_x_1,point_y_1,point_x_2,point_y_2):
    A =float(point_y_2 - point_y_1)
    B =float(point_x_1 - point_x_2)
    C =float(point_x_2 * point_y_1 - point_x_1 * point_y_2)
    return '('+str(A)+')'+'x + '+'('+str(B)+')'+'y + '+'('+str(C)+')'+' = 0'

while True:

    init()

    print(Fore.CYAN)

    count_points=int(input('Введите количество точек (3-5) => '))

    if count_points==3:
        print('Введите координаты точек: ')

        x1, y1= input('Точка А => ').split(';')
        x2, y2= input('Точка B => ').split(';')
        x3, y3= input('Точка C => ').split(';')

        x1,x2,x3=float(x1), float(x2), float(x3)
        y1,y2,y3=float(y1), float(y2), float(y3)

        if (x1==x2==x3) or (y1==y2==y3):
             print('Такого треугольника не существует!')
             continue

        AB=side(point_x_1=x1,point_y_1=y1,point_x_2=x2,point_y_2=y2)
        BC=side(point_x_1=x2,point_y_1=y2,point_x_2=x3,point_y_2=y3)
        AC=side(point_x_1=x1,point_y_1=y1,point_x_2=x3,point_y_2=y3)

        AF=lenght_median(side1=AC,side2=AB,side3=BC)#math.sqrt(2*AC**2+2*AB**2-BC**2)/2#AC AB BC
        BD=lenght_median(side1=AC,side2=BC,side3=AB)#math.sqrt(2*AC**2+2*BC**2-AB**2)/2#AC BC AB
        CE=lenght_median(side1=AB,side2=BC,side3=AC)#math.sqrt(2*AB**2+2*BC**2-AC**2)/2#AB BC AC

        angle_BAC=angle(side1=AC,side2=AB,side3=BC)#degrees(acos((AC**2+AB**2-BC**2)/(2.0 * AB * AC)))
        angle_ABC=angle(side1=AC,side2=BC,side3=AB)#degrees(acos((AC**2+BC**2-AB**2)/(2.0 * AC * BC)))
        angle_BCA=angle(side1=AB,side2=BC,side3=AC)#degrees(acos((AB**2+BC**2-AC**2)/(2.0 * AB * BC)))

        # наименование точек
        fig, ax = plt.subplots()

        ax.text(x1-0.05,y1-0.05, 'A',style ='italic',fontsize = 15, color="purple")
        ax.text(x2-0.05,y2+0.05, 'B',style ='italic',fontsize = 15, color="purple")
        ax.text(x3+0.05,y3-0.05, 'C',style ='italic',fontsize = 15, color="purple")

        ax.text(((x2 + x3)/2)+0.05,((y2 + y3)/2), 'F',style ='italic',fontsize = 15, color="purple")
        ax.text(((x1 + x3)/2),((y1 + y3)/2)-0.05, 'D',style ='italic',fontsize = 15, color="purple")
        ax.text(((x1 + x2)/2)-0.05,((y1 + y2)/2), 'E',style ='italic',fontsize = 15, color="purple")

        #Медианы углов А, В, С
        mid_BC_x,mid_BC_y=((x2 + x3)/2),((y2 + y3)/2)
        median_A_x,median_A_y=[x1,mid_BC_x],[y1,mid_BC_y]

        mid_AC_x,mid_AC_y=((x1 + x3)/2),((y1 + y3)/2)
        median_B_x,median_B_y=[x2,mid_AC_x],[y2,mid_AC_y]

        mid_AB_x,mid_AB_y=((x1 + x2)/2),((y1 + y2)/2)
        median_C_x,median_C_y=[x3,mid_AB_x],[y3,mid_AB_y]

        print(Fore.GREEN)

        print('Информация о треугольнике:')
        if (AB+BC>AC) and (BC+AC>AB) and (AB+AC>BC):
             if AB == BC == AC:
                  print('Тип >> "Равносторонний треугольник"')
             elif (angle_BAC==90) or (angle_ABC==90) or (angle_BCA==90):
                  print('Тип >> "Прямоугольный треугольник"')
             elif (angle_BAC<90) and (angle_ABC<90) and (angle_BCA<90):
                  print('Тип >> "Остроугольный треугольник"')
             elif (angle_BAC > 90) or (angle_ABC > 90) or (angle_BCA > 90):
                  print('Тип >> "Тупоугольный треугольник"')
             elif (AB!=BC==AC) or (AB==BC!=AC) or (AB==AC!=BC):
                  print('Тип >> Равнобедренный треугольник')
             print('Площадь треугольника >> '+str('%.2f' %square(AB, BC, AC))+'см')
             print('Периметр треугольника >> '+str('%.2f' %perimeter(AB, BC, AC))+'см')

        else:
             print('Такого треугольника не существует!')
             continue

        print(Fore.BLUE)

        print('Углы треугольника:')
        print('∠BAC >> '+str('%.2f' %angle_BAC)+'°')
        print('∠ABC >> '+str('%.2f' %angle_ABC)+'°')
        print('∠BCA >> '+str('%.2f' %angle_BCA)+'°')

        print(Fore.MAGENTA)

        print('Стороны треугольника:')
        print('АВ >> '+str('%.2f' %AB)+'см')
        print('ВC >> '+str('%.2f' %BC)+'см')
        print('АC >> '+str('%.2f' %AC)+'см')

        print(Fore.MAGENTA)

        print('Длины медиан:')
        print('AF >> '+str('%.2f' %AF)+'см')
        print('BD >> '+str('%.2f' %BD)+'см')
        print('CE >> '+str('%.2f' %CE)+'см')

        print(Fore.MAGENTA)

        print('Уравнения сторон треугольника:')
        print('AB >> '+ equation_side(point_x_1=x1,point_y_1=y1,point_x_2=x2,point_y_2=y2))
        print('BC >> '+ equation_side(point_x_1=x2,point_y_1=y2,point_x_2=x3,point_y_2=y3))
        print('AC >> '+ equation_side(point_x_1=x1,point_y_1=y1,point_x_2=x3,point_y_2=y3))

        #print(''+str(r))
        x, y = [x1, x2, x3], [y1, y2, y3]
        x1, y1 = [x1, x3], [y1, y3]

        plt.plot(x,y, color='black')
        plt.plot(x1,y1, color='black')
        plt.plot(x,y,'o')
        plt.plot(x1,y1,'o')

        plt.plot(median_A_x,median_A_y, color='blue')
        plt.plot(median_A_x,median_A_y,'o')

        plt.plot(median_B_x,median_B_y, color='blue')
        plt.plot(median_B_x,median_B_y,'o')

        plt.plot(median_C_x,median_C_y, color='blue')
        plt.plot(median_C_x,median_C_y,'o')

        ax.grid()
        plt.title('Ваш треугольник:')
        plt.show()
    elif count_points==4:
        print('Введите координаты точек: ')

        x1, y1 = input('Точка А => ').split(';')
        x2, y2 = input('Точка B => ').split(';')
        x3, y3 = input('Точка C => ').split(';')
        x4, y4 = input('Точка D => ').split(';')

        x1, x2, x3, x4 = float(x1), float(x2), float(x3), float(x4)
        y1, y2, y3, y4 = float(y1), float(y2), float(y3), float(y4)
        AB=side(point_x_1=x1,point_y_1=y1,point_x_2=x2,point_y_2=x3)
        BC=side(point_x_1=x2,point_y_1=y2,point_x_2=x3,point_y_2=y3)
        CD=side(point_x_1=x3,point_y_1=y3,point_x_2=x4,point_y_2=y4)
        AD=side(point_x_1=x1,point_y_1=y1,point_x_2=x4,point_y_2=y4)

        AC=side(point_x_1=x2,point_y_1=y2,point_x_2=x4,point_y_2=x4)
        BD=side(point_x_1=x1,point_y_1=y1,point_x_2=x3,point_y_2=x3)

        #Точка пересечения диагоналей
        mid_diag_x, mid_diag_y = ((x2+x4)/2),((y2+x4)/2)

    elif count_points==5:
    break