import math
choice=int(input('Введите тип ввода ( По координатам (Напиши 1) / По сторонам треугольника (Напиши 2) ) => '))
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
          print('Площадь треугольника: ', ((AB**2)*math.sqrt(3))/4)
          print('Периметр треугольника: ', AB+BC+AC)
     elif (AB!=BC==AC) or (AB==BC!=AC) or (AB!=AC==BC):
          print('Тип: "Равнобедренный треугольник"')
     if AB!=BC==AC:
          print('Площадь треугольника: ', (math.sqrt(4*(BC**2)-(AB**2)))/2)
          print('Периметр треугольника: ', AB + BC + AC)
     elif AB==BC!=AC:
          print('Площадь треугольника: ', (math.sqrt(4 * (BC ** 2) - (AC ** 2))) / 2)
          print('Периметр треугольника: ', AB + BC + AC)
     elif AB!=AC==BC:
          print('Площадь треугольника: ', (math.sqrt(4*(BC**2)-(AB**2)))/2)
          print('Периметр треугольника: ', AB + BC + AC)
     elif AB!=BC!=AC:
          list1=[AB, BC, AC]
          min_side=min(list1)
          mid_side=sum(list1)-min(list1)-max(list1)
          max_side=max(list1)
          if max_side**2==mid_side**2+min_side**2:
               print('Тип: "Прямоугольный треугольник"')
               print('Площадь треугольника: ',(mid_side*min_side)/2)
               print('Периметр треугольника: ', mid_side + min_side + max_side)
          elif max_side**2<mid_side**2+min_side**2:
               print('Тип: "Остроугольный треугольник"')
               p = (mid_side + min_side + max_side) / 2
               print('Площадь треугольника: ', math.sqrt(p * (p - min_side) * (p - mid_side) * (p - max_side)))
               print('Периметр треугольника: ', mid_side + min_side + max_side)
          elif max_side**2>mid_side**2+min_side**2:
               print('Тип: "Тупоугольный треугольник"')
               p=(mid_side+min_side+max_side)/2
               print('Площадь треугольника: ',math.sqrt(p*(p-min_side)*(p-mid_side)*(p-max_side)))
               print('Периметр треугольника: ',mid_side+min_side+max_side)
else:
     print('Такого треугольника не существует!')