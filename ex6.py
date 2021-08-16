# Пользователь вводит номер буквы в алфавите. Определить, какая это буква.

while True:
    try:
        a = int(input('Введите номер буквы в английском алфавита: '))
        if a > 26 or a < 1:
            raise ValueError
        else:
            print(chr(a + 64))
    except ValueError:
        print('Нет такой буквы в алфавите')
    break
