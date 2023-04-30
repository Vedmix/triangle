from math import acos, degrees, sqrt, sin

def side(point_x_1, point_y_1, point_x_2, point_y_2):
    side = sqrt(((point_x_1 - point_x_2) ** 2) + ((point_y_1 - point_y_2) ** 2))
    return side

def perimeter_t(side1, side2, side3):
    return float((side1+side2+side3))

def perimeter_e(side1, side2, side3,side4):
    return float((side1+side2+side3+side4))

def square(side1, side2, side3):
    p = perimeter_t(side1, side2, side3) / 2
    return (sqrt(p * (p - side1) * (p - side2) * (p - side3)))

def lenght_median(side1, side2, side3):  # side3 вычитаем
    lenght_median = sqrt(2 * side1 ** 2 + 2 * side2 ** 2 - side3 ** 2) / 2
    return lenght_median

def angle(side1, side2, side3):  # side3 вычитаем
    angle = (acos((side1 ** 2 + side2 ** 2 - side3 ** 2) / (2.0 * side1 * side2)))
    return angle

def equationYKB(x1, y1, x2, y2):
    if x2 == x1:
        return f"x = {'%.2F' %x1}"
    if y2 == y1:
        return f"y = {'%.2F' %y1}"
    k = (y2 - y1) / (x2 - x1)
    b = y1 - k * x1
    if b<0:
        return f"y = {'%.2F' %k}x + ({'%.2F' %b})"
    else:
        return f"y = {'%.2F' %k}x + {'%.2F' %b}"

def equationABC(point_x_1, point_y_1, point_x_2, point_y_2):
    A = float(point_y_2 - point_y_1)
    B = float(point_x_1 - point_x_2)
    C = float(point_x_2 * point_y_1 - point_x_1 * point_y_2)
    return '(' + str(A) + ')' + 'x + ' + '(' + str(B) + ')' + 'y + ' + '(' + str(C) + ')' + ' = 0'

def equationH(point_x_1, point_y_1, point_x_2, point_y_2,x1,y1):
    A = float(point_y_2 - point_y_1)
    B = float(point_x_1 - point_x_2)
    C = float(point_x_2 * point_y_1 - point_x_1 * point_y_2)
    a=-B
    b=A
    c=b*x1-a*y1
    return '(' + str(a) + ')' + 'x + ' + '(' + str(b) + ')' + 'y + ' + '(' + str(c) + ')' + ' = 0'

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