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

def card_player_1(mean, suit):
    # Присовение масти к номеру

    if card_suit_1 == 1:
        suit = 'Черви'
    elif card_suit_1 == 2:
        suit = 'Буби'
    elif card_suit_1 == 3:
        suit = 'Крести'
    elif card_suit_1 == 4:
        suit = 'Пики'

    # Присвоение достоинства карты к номеру

    if card_mean_1 == 6:
        mean = 'Шестерка'
    elif card_mean_1 == 7:
        mean = 'Семерка'
    elif card_mean_1 == 8:
        mean = 'Восьмерка'
    elif card_mean_1 == 9:
        mean = 'Девятка'
    elif card_mean_1 == 10:
        mean = 'Десятка'
    elif card_mean_1 == 11:
        mean = 'Валет'
    elif card_mean_1 == 12:
        mean = 'Дама'
    elif card_mean_1 == 13:
        mean = 'Король'
    elif card_mean_1 == 14:
        mean = 'Туз'

    return (mean, suit)

def card_player_2(mean, suit):
    # Присовение масти к номеру

    if card_suit_2 == 1:
        suit = 'Черви'
    elif card_suit_2 == 2:
        suit = 'Буби'
    elif card_suit_2 == 3:
        suit = 'Крести'
    elif card_suit_2 == 4:
        suit = 'Пики'

    # Присвоение достоинства карты к номеру

    if card_mean_2 == 6:
        mean = 'Шестерка'
    elif card_mean_2 == 7:
        mean = 'Семерка'
    elif card_mean_2 == 8:
        mean = 'Восьмерка'
    elif card_mean_2 == 9:
        mean = 'Девятка'
    elif card_mean_2 == 10:
        mean = 'Десятка'
    elif card_mean_2 == 11:
        mean = 'Валет'
    elif card_mean_2 == 12:
        mean = 'Дама'
    elif card_mean_2 == 13:
        mean = 'Король'
    elif card_mean_2 == 14:
        mean = 'Туз'

    return (mean, suit)

player_one_card = card_player_1(mean=card_mean_1, suit=card_suit_1)

card_suit_2 = randint(1, 4)
card_mean_2 = randint(6, 14)

player_two_card = card_player_2(mean=card_mean_2, suit=card_suit_2)


print(player1, 'выпала карта', player_one_card)
print(player2, 'выпала карта', player_two_card)

# сравнение карт

if card_mean_1 < card_mean_2:
    print('Карта игрока', player2, 'старше, он победил.')
elif card_mean_1 > card_mean_2:
    print('Карта игрока', player1, 'старше, он победил.')
elif card_mean_1 == card_mean_2:
    if card_suit_1 > card_suit_2:
        print('Карта игрока', player1, 'старше, он победил.')
    elif card_suit_1 < card_suit_2:
        print('Карта игрока', player2, 'старше, он победил.')
    else:
        print('Вот и попались шулеры.. =)')