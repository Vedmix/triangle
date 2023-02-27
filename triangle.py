import math
a=int(input(''))
if a==1:
     print('')
elif a==2:
     print('')
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
     minStr=min(list1)
     srStr=sum(list1)-min(list1)-max(list1)
     maxStr=max(list1)
     if maxStr**2==srStr**2+minStr**2:
          print('Прямоугольный треугольник')
     elif maxStr**2<srStr**2+minStr**2:
          print('Остроугольный треугольник')
     elif maxStr**2>srStr**2+minStr**2:
          print('Тупоугольный треугольник')
print(minStr)
print(srStr)
print(maxStr)
print(AB)
print(BC)
print(AC)
