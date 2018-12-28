from random import randint
import time

player1 = input('Имя первого игрока:')
print('Привет,', player1)
time.sleep(1)
player2 = input('Имя второго игрока:')
print('Привет,', player2)

# масть карт от 1 до 4
# достоинство карты от 1 до 9

card_suit_1 = randint(1, 4)
card_mean_1 = randint(6, 14)

#  определение масти карты

card_suit_player_one = ['Черви', 'Буби', 'Крести', 'Пики']

for suit in card_suit_player_one:
    card_suit_1 = suit

# определение достоинства карты

card_mean_player_one = ['Шестерка', 'Семерка', 'Восьмерка', 'Девятка', 'Десятка', 'Валет', 'Дама', 'Король', 'Туз']

for mean in card_mean_player_one:
    card_mean_1 = mean

print('Игроку', player1, 'выпала карта', card_mean_1, card_suit_1)

# тоже самое для второго игрока

card_suit_2 = randint(1, 4)
card_mean_2 = randint(6, 14)

#  определение масти карты

card_suit_player_two = ['Черви', 'Буби', 'Крести', 'Пики']

for suit in card_suit_player_two:
    card_suit_2 = suit

# определение достоинства карты

card_mean_player_two = ['Шестерка', 'Семерка', 'Восьмерка', 'Девятка', 'Десятка', 'Валет', 'Дама', 'Король', 'Туз']

for mean in card_mean_player_two:
    card_mean_2 = mean

print('Игроку', player2, 'выпала карта', card_mean_2, card_suit_2)

if card_mean_1 > card_mean_2:
    print('Победа за игроком ', player1)
elif card_mean_1 < card_mean_2:
    print('Победа за игроком ', player2)
elif card_mean_1 == card_mean_2:
    if card_suit_1 > card_suit_2:
        print('Победа за игроком ', player1)
    else:
        print('Победа за игроком ', player2)
else:
    print('Что то пошло не так')


