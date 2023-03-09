import matplotlib.pyplot as plt
import math
from math import acos, degrees
from colorama import init
from colorama import Fore, Back, Style

def perimeter(AB, BC, AC):
     return float('%.2f'%(AB+BC+AC))
def square(AB, BC, AC):
     p=perimeter(AB, BC, AC)/2
     return '%.2f'%(math.sqrt(p*(p-AB)*(p-BC)*(p-AC)))

init()
print(Fore.CYAN)

print('Введите координаты точек: ')
x1, y1= input('Точка А => ').split(';')
x2, y2= input('Точка B => ').split(';')
x3, y3= input('Точка C => ').split(';')

x1,x2,x3=float(x1), float(x2), float(x3)
y1,y2,y3=float(y1), float(y2), float(y3)

if (x1==x2==x3) or (y1==y2==y3):
     print('Такого треугольника не существует!')

AB=math.sqrt(((x1-x2)**2)+((y1-y2)**2))
BC=math.sqrt(((x2-x3)**2)+((y2-y3)**2))
AC=math.sqrt(((x1-x3)**2)+((y1-y3)**2))

list1 = [AB, BC, AC]
min_side = min(list1)
mid_side = sum(list1) - min(list1) - max(list1)
max_side = max(list1)

print(Fore.GREEN)

print('Информация о треугольнике:')
if (AB+BC>AC) and (BC+AC>AB) and (AB+AC>BC):
     if AB == BC == AC:
          print('Тип >> "Равносторонний треугольник"')
     if (max_side**2==mid_side**2+min_side**2):
          print('Тип >> "Прямоугольный треугольник"')
     elif (AB!=BC==AC) or (AB==BC!=AC) or (AB==AC!=BC):
          print('Тип >> Равнобедренный треугольник')
     print('Площадь треугольника >> ', square(AB, BC, AC))
     print('Периметр треугольника >>', perimeter(AB, BC, AC))

else:
     print('Такого треугольника не существует!')

print(Fore.BLUE)

print('Углы треугольника:')
angle_BAC=degrees(acos((AC**2+AB**2-BC**2)/(2.0 * AB * AC)))
angle_ABC=degrees(acos((AC**2+BC**2-AB**2)/(2.0 * AC * BC)))
angle_BCA=degrees(acos((AB**2+BC**2-AC**2)/(2.0 * AB * BC)))
print('∠BAC >> '+str(round(angle_BAC,1))+'°')
print('∠ABC >> '+str(round(angle_ABC,1))+'°')
print('∠BCA >> '+str(round(angle_BCA,1))+'°')

print(Fore.MAGENTA)

print('Стороны треугольника:')
print('АВ >> '+str(round(AB,1))+'см')
print('ВC >> '+str(round(BC,1))+'см')
print('АC >> '+str(round(AC,1))+'см')

#Медиана угла А
mid_BC_x,mid_BC_y=((x2 + x3)/2),((y2 + y3)/2)
median_A_x,median_A_y=[x1,mid_BC_x],[y1,mid_BC_y]
#Медиана угла B
mid_AC_x,mid_AC_y=((x1 + x3)/2),((y1 + y3)/2)
median_B_x,median_B_y=[x2,mid_AC_x],[y2,mid_AC_y]
#Медиана угла C
mid_AB_x,mid_AB_y=((x1 + x2)/2),((y1 + y2)/2)
median_C_x,median_C_y=[x3,mid_AB_x],[y3,mid_AB_y]
#3 стороны треугольника
x,y=[x1,x2,x3],[y1,y2,y3]
x1,y1=[x1,x3],[y1,y3]

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
plt.title('Ваш треугольник:')
plt.show()