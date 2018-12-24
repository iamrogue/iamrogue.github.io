from random import randint
import time

print('Компьютер загадывает число...')
time.sleep(2)
number = randint(1, 101)
print('Готово, начинай отгадывать...')

tries = 0   # Кол-во попыток

while tries <= 6:
    answer = int(input('Твое число - '))
    tries += 1
    if answer == number:
        print('Угадал!')
        print('Отгадал с', tries, 'раза.')
        break
    elif answer < number:
        print('Бооольшееее')
    elif answer > number:
        print('Меньше!!!')

print('Попытки закончились...')

