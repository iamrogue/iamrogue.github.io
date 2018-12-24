from random import randint

# otvet = int(input('Четное число или нечетное: '))
# n_comp = randint(1, 2)
# if otvet != 1 and otvet != 2:
#     print('введите число 1 или 2')
# elif otvet == n_comp:
#     print('Выйграл')
# else:
#     print('Проиграл')


n = 5     # кол-во попыток
k = 0     # счетчик

for m in range(n):
    while True:
        number = int(input('Введите число 1 или 2: '))
        if number != 1 and number != 2:
            print('Введите числа 1 или 2')
        else:
            break     # вышли из while
    n_comp = randint(1, 2)
    print('Рандомное число: ', n_comp)
    if number == n_comp:
        k += 1
        if k > n//2:
            print('Счет ', number, ':', n_comp, ' в вашу пользу.')
        else:
            print('Счет ', n_comp, ':', number, ' в пользу компьютера.')    # надо переделать, пока не придумал как