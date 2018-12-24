from random import randint
import time

player1 = input('Имя первого игрока:')
print('Привет,', player1)
time.sleep(1)
player2 = input('Имя второго игрока:')
print('Привет,', player2)

# масть карт от 1 до 4
# достоинство карты от 1 до 9

card_suit = randint(1, 4)
card_mean = randint(6, 14)

def card_player(mean, suit):
    # Присовение масти к номеру

    if card_suit == 1:
        suit = 'Черви'
    elif card_suit == 2:
        suit = 'Буби'
    elif card_suit == 3:
        suit = 'Крести'
    elif card_suit == 4:
        suit = 'Пики'

    # Присвоение достоинства карты к номеру

    if card_mean == 6:
        mean = 'Шестерка'
    elif card_mean == 7:
        mean = 'Семерка'
    elif card_mean == 8:
        mean = 'Восьмерка'
    elif card_mean == 9:
        mean = 'Девятка'
    elif card_mean == 10:
        mean = 'Десятка'
    elif card_mean == 11:
        mean = 'Валет'
    elif card_mean == 12:
        mean = 'Дама'
    elif card_mean == 13:
        mean = 'Король'
    elif card_mean == 14:
        mean = 'Туз'

    return (mean, suit)

player_one_card = card_player(mean=card_mean, suit=card_suit)

card_suit = randint(1, 4)
card_mean = randint(6, 14)

player_two_card = card_player(mean=card_mean, suit=card_suit)


print(player1, 'выпала карта', player_one_card)
print(player2, 'выпала карта',player_two_card)

# сравнение карт

