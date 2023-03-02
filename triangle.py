import matplotlib.pyplot as plt
import math
def perimeter(AB, BC, AC):
     return float('%.2f'%(AB+BC+AC))
def square(AB, BC, AC):
     p=perimeter(AB, BC, AC)/2
     return '%.2f'%(math.sqrt(p*(p-AB)*(p-BC)*(p-AC)))
print('Усложнённый вариант >> По координатам (Напиши 1)')
print('Упрощенный вариант >> По сторонам треугольника (Напиши 2)')
choice=int(input('Введите тип ввода => '))
if choice==2:
     AB=float(input('Сторона АВ => '))
     BC=float(input('Сторона ВC => '))
     AC=float(input('Сторона АC => '))
elif choice==1:
     print('Введите координаты точек: ')
     x1, y1= input('Точка А => ').split(';')
     x2, y2= input('Точка B => ').split(';')
     x3, y3= input('Точка C => ').split(';')
     x1,x2,x3=float(x1), float(x2), float(x3)
     y1,y2,y3=float(y1), float(y2), float(y3)
     AB=math.sqrt(((x1-x2)**2)+((y1-y2)**2))
     BC=math.sqrt(((x2-x3)**2)+((y2-y3)**2))
     AC=math.sqrt(((x1-x3)**2)+((y1-y3)**2))
print('Информация о треугольнике:')
if (AB+BC>AC) and (BC+AC>AB) and (AB+AC>BC):
     if AB == BC == AC:
          print('Тип: "Равносторонний треугольник"')
          print('Площадь треугольника: ', square(AB, BC, AC))
          print('Периметр треугольника: ', perimeter(AB, BC, AC))
     elif (AB!=BC==AC) or (AB==BC!=AC) or (AB!=AC==BC):
          print('Тип: "Равнобедренный треугольник"')
          print('Площадь треугольника: ', square(AB, BC, AC))
          print('Периметр треугольника: ', perimeter(AB, BC, AC))
     else:
          list1=[AB, BC, AC]
          min_side=min(list1)
          mid_side=sum(list1)-min(list1)-max(list1)
          max_side=max(list1)
          if max_side**2==mid_side**2+min_side**2:
               print('Тип: "Прямоугольный треугольник"')
               print('Площадь треугольника: ',square(AB, BC, AC))
               print('Периметр треугольника: ',perimeter(AB, BC, AC))
          elif max_side**2<mid_side**2+min_side**2:
               print('Тип: "Остроугольный треугольник"')
               print('Площадь треугольника: ',square(AB, BC, AC))
               print('Периметр треугольника: ',perimeter(AB, BC, AC))
          elif max_side**2>mid_side**2+min_side**2:
               print('Тип: "Тупоугольный треугольник"')
               print('Площадь треугольника: ',square(AB, BC, AC))
               print('Периметр треугольника: ',perimeter(AB, BC, AC))
else:
     print('Такого треугольника не существует!')

x=[x1,x2,x3]
y=[y1,y2,y3]
fig, ax = plt.subplots()
plt.fill(x,y)
ax.grid()
plt.show()

