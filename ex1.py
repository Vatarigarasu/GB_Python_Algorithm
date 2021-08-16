from functools import reduce

while True:
    try:
        a = input('Введите трехзначное число: ')
        if len(a) != 3:
            raise ValueError
        else:
            My_list = [int(i) for i in a]
            print(My_list)
            print(sum(My_list))
            print(reduce(lambda x, y: x * y, My_list))
    except ValueError:
        print('Неверная длина числа')
    break
