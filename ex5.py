# Пользователь вводит две буквы. Определить, на каких местах алфавита они стоят, и сколько между ними находится букв.

while True:
    try:
        a = int(ord(input('Введите первую букву: ').capitalize()))
        b = int(ord(input('Введите вторую букву: ').capitalize()))
        if a > 90 or a < 65 or b > 90 or b < 65:
            raise ValueError
        else:
            print('Номер первой буквы: ', a-64)
            print('Номер второй буквы: ', b-64)
            print(f'Между буквами {abs(a-b)} букв')
    except ValueError:
        print("Неверные буквы!")
    break


