# По введенным пользователем координатам двух точек вывести уравнение прямой вида y = kx + b, проходящей через эти точки

x1 = int(input('Введите X координату первой точки'))
y1 = int(input('Введите Y координату первой точки'))
x2 = int(input('Введите X координату второй точки'))
y2 = int(input('Введите Y координату второй точки'))
print(x1)
print(y1)
print(x2)
print(y2)
k = (y2-y1)/(x2-x1)
b = y2-y1/x1*x2
print(f'y = {k}x + {b}')
