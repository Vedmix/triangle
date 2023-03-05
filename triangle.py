import matplotlib.pyplot as plt
import math
from colorama import init
from colorama import Fore, Back, Style
import numpy as np
def perimeter(AB, BC, AC):
     return float('%.2f'%(AB+BC+AC))
def square(AB, BC, AC):
     p=perimeter(AB, BC, AC)/2
     return '%.2f'%(math.sqrt(p*(p-AB)*(p-BC)*(p-AC)))

init()
print(Fore.CYAN)
print('Режимы работы программы:')
print('Упрощенный режим (по сторонам треугольника) >> (Напиши 1 )')
print('Усложнённый режим (по координатам) >>(Напиши 2 )')
print('Информация о программе >> (Напиши 3)')

choice=int(input('Введите режим=> '))
if choice==1:
     print('Введите стороны треугольника:')
     AB=float(input('Сторона АВ => '))
     BC=float(input('Сторона ВC => '))
     AC=float(input('Сторона АC => '))
elif choice==2:
     print('Введите координаты точек: ')
     x1, y1= input('Точка А => ').split(';')
     x2, y2= input('Точка B => ').split(';')
     x3, y3= input('Точка C => ').split(';')

     x1,x2,x3=float(x1), float(x2), float(x3)
     y1,y2,y3=float(y1), float(y2), float(y3)

     AB=math.sqrt(((x1-x2)**2)+((y1-y2)**2))
     BC=math.sqrt(((x2-x3)**2)+((y2-y3)**2))
     AC=math.sqrt(((x1-x3)**2)+((y1-y3)**2))

     list1 = [AB, BC, AC]
     min_side = min(list1)
     mid_side = sum(list1) - min(list1) - max(list1)
     max_side = max(list1)
elif choice==3:
     print('Скоро будет')

print('Информация о треугольнике:')
if (AB+BC>AC) and (BC+AC>AB) and (AB+AC>BC):
     if AB == BC == AC:
          print('Тип: "Равносторонний треугольник"')
     if (max_side**2==mid_side**2+min_side**2):
          print('Тип: "Прямоугольный треугольник"')
     elif (AB!=BC==AC) or (AB==BC!=AC) or (AB==AC!=BC):
          if (max_side**2<mid_side**2+min_side**2):
               angle_type = 'острым'
          elif (max_side**2==mid_side**2+min_side**2):
               angle_type = 'прямым'
          elif (max_side**2 > mid_side**2+min_side**2):
               angle_type = 'тупым'
     print('Тип: Равнобедренный треугольник c '+angle_type+' углом')
     print('Площадь треугольника: ', square(AB, BC, AC))
     print('Периметр треугольника: ', perimeter(AB, BC, AC))

else:
     print('Такого треугольника не существует!')
#Медиана угла А
mid_BC_x=((x2 + x3)/2.0)
mid_BC_y=((y2 + y3)/2.0)
median_A_x=[x1,mid_BC_x]
median_A_y=[y1,mid_BC_y]
#Медиана угла B
mid_AC_x=((x1 + x3)/2.0)
mid_AC_y=((y1 + y3)/2.0)
median_B_x=[x2,mid_AC_x]
median_B_y=[y2,mid_AC_y]
#Медиана угла C
mid_AB_x=((x1 + x2)/2.0)
mid_AB_y=((y1 + y2)/2.0)
median_C_x=[x3,mid_AB_x]
median_C_y=[y3,mid_AB_y]

#3 стороны треугольника
x=[x1,x2,x3]
y=[y1,y2,y3]
x1=[x1,x3]
y1=[y1,y3]

fig, ax = plt.subplots()
plt.plot(x,y, color='black')
plt.plot(x1,y1, color='black')
plt.plot(x,y,'o')
plt.plot(x1,y1,'o')

plt.plot(median_A_x,median_A_y, color='black')
plt.plot(median_A_x,median_A_y,'o')

plt.plot(median_B_x,median_B_y, color='black')
plt.plot(median_B_x,median_B_y,'o')

plt.plot(median_C_x,median_C_y, color='black')
plt.plot(median_C_x,median_C_y,'o')

ax.grid()
plt.title('Твой треугольник:')
plt.show()

