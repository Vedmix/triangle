import math
choice=input('Введите тип ввода ( По координатам/По сторонам треугольника ):')
if choice=='По сторонам треугольника':
     AB=float(input())
     BC=float(input())
     AC=float(input())
elif choice=='По координатам':
     x1, y1= input().split(';')
     x2, y2= input().split(';')
     x3, y3= input().split(';')
     x1,x2,x3=float(x1), float(x2), float(x3)
     y1,y2,y3=float(y1), float(y2), float(y3)
     AB=math.sqrt(((x1-x2)**2)+((y1-y2)**2))
     BC=math.sqrt(((x2-x3)**2)+((y2-y3)**2))
     AC=math.sqrt(((x1-x3)**2)+((y1-y3)**2))
if AB==BC==AC:
     print('Равносторонний треугольник')
elif (AB!=BC==AC) or (AB==BC!=AC) or (AB!=AC==BC):
     print('Равнобедренный треугольник')
elif AB!=BC!=AC:
     list1=[AB, BC, AC]
     min_side=min(list1)
     mid_side=sum(list1)-min(list1)-max(list1)
     max_side=max(list1)
     if max_side**2==mid_side**2+min_side**2:
          print('Прямоугольный треугольник')
     elif max_side**2<mid_side**2+min_side**2:
          print('Остроугольный треугольник')
     elif max_side**2>mid_side**2+min_side**2:
          print('Тупоугольный треугольник')
