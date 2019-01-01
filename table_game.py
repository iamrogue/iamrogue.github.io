from random import randint
import time

player = input('Введите ваше имя: ')
time.sleep(2)

n = randint(15, 25)     # количество предметов
k = randint(3, 5)

print('На столе всего', n, 'предметов')

turn = randint(1, 2)
if turn == 1:
    print('Ходит', player)
else:
    print('Ход компьютера')

print('Можно взять не более', k, 'предметов.')

time.sleep(2)

while True:
    if turn == 1:
        if n >= k:
            pc_take = randint(1, k)
        else:
            pc_take = randint(1, n)
        time.sleep(2)
        print('Компьютер взял', pc_take, 'предметов.')
        n = n - pc_take
    else:
        player_take = int(input('Сколько предметов вы берете?'))
        n = n - player_take
    if n == 0:
        if turn == 2:
            print(player, 'взял последний предмет, значит выйграл компьютер.')
            break
        else:
            print('Последний предмет взял компьютер, значит выйграл', player)
            break
    else:
        print('На столе соталось', n, 'предметов, игра продолжается')
        if turn == 2:
            turn = 1
        else:
            turn = 2