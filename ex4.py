# Написать программу, которая генерирует в указанных пользователем границах:
# случайное целое число;
# случайное вещественное число;
# случайный символ.

from random import randint, uniform
case = input('Введите код операции:')
if case == '1':
    lower_limit = int(input('Введите нижнюю границу: '))
    upper_limit = int(input('Введите нижнюю границу: '))
    print(randint(lower_limit, upper_limit))
elif case == '2':
    lower_limit = int(input('Введите нижнюю границу: '))
    upper_limit = int(input('Введите нижнюю границу: '))
    print(uniform(lower_limit, upper_limit))
elif case == '3':
    lower_limit = int(input('Введите нижнюю границу: '))
    upper_limit = int(input('Введите нижнюю границу: '))
    print(chr(randint(lower_limit, upper_limit)))
elif case == 'help' or '' or ' ':
    print('Коды операций: \n'
             '"1" для случайного целого числа \n'
             '"2" для случайного вещественного числа \n'
             '"3" для случайного символа')
