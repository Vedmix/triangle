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

fig, ax = plt.subplots()

ax.text(x1-0.05,y1-0.05, 'A',style ='italic',fontsize = 15, color="purple")
ax.text(x2-0.05,y2+0.05, 'B',style ='italic',fontsize = 15, color="purple")
ax.text(x3+0.05,y3-0.05, 'C',style ='italic',fontsize = 15, color="purple")

AB=math.sqrt(((x1-x2)**2)+((y1-y2)**2))
BC=math.sqrt(((x2-x3)**2)+((y2-y3)**2))
AC=math.sqrt(((x1-x3)**2)+((y1-y3)**2))

AF=math.sqrt(2*AC**2+2*AB**2-BC**2)/2
BD=math.sqrt(2*AC**2+2*BC**2-AB**2)/2
CE=math.sqrt(2*AB**2+2*BC**2-AC**2)/2

AB_A=y2-y1
AB_B=x1-x2
AB_C=x2*y1-x1*y2

BC_A=y3-y2
BC_B=x2-x3
BC_C=x3*y2-x2*y3

AC_A=y3-y1
AC_B=x1-x3
AC_C=x3*y1-x1*y3

#min_circle_radius=(AB*BC)/(AB+BC+AC)
#min_circle_radius=(AB+BC-AC)/2
#min_circle_radius=(square(AB, BC, AC))/(perimeter(AB, BC, AC)/2)

ax.text(((x2 + x3)/2)+0.05,((y2 + y3)/2), 'F',style ='italic',fontsize = 15, color="purple")
ax.text(((x1 + x3)/2),((y1 + y3)/2)-0.05, 'D',style ='italic',fontsize = 15, color="purple")
ax.text(((x1 + x2)/2)-0.05,((y1 + y2)/2), 'E',style ='italic',fontsize = 15, color="purple")

angle_BAC=degrees(acos((AC**2+AB**2-BC**2)/(2.0 * AB * AC)))
angle_ABC=degrees(acos((AC**2+BC**2-AB**2)/(2.0 * AC * BC)))
angle_BCA=degrees(acos((AB**2+BC**2-AC**2)/(2.0 * AB * BC)))

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

print(Fore.GREEN)

print('Информация о треугольнике:')
if (AB+BC>AC) and (BC+AC>AB) and (AB+AC>BC):
     if AB == BC == AC:
          print('Тип >> "Равносторонний треугольник"')
     if (angle_BAC==90) or (angle_ABC==90) or (angle_BCA==90):
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
print('AB >> '+'('+str(AB_A)+')'+'x + '+'('+str(AB_B)+')'+'y + '+'('+str(AB_C)+')'+" = 0")
print('BC >> '+'('+str(BC_A)+')''x + '+'('+str(BC_B)+')'+'y + '+'('+str(BC_C)+')'+" = 0")
print('AC >> '+'('+str(AC_A)+')'+'x + '+'('+str(AC_B)+')'+'y + '+'('+str(AC_C)+')'+" = 0")

#print('%.2f' %min_circle_radius)
# print(equation(x1,x2,y1,y2))

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