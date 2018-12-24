from random import randint
import time

player1 = input("Enter player's one name: ")
print('Hi, ', player1)
time.sleep(2)
player2 = input("Enter player's two name: ")
print('Hi, ', player2)
time.sleep(2)

print('Turn ONE of the player', player1)
time.sleep(3)
num1_pl_one = randint(1, 6)
print('It is: ', num1_pl_one)
print('Turn TWO of the player', player1)
time.sleep(3)
num2_pl_one = randint(1, 6)
print('It is: ', num2_pl_one)
sum_pl_one = num1_pl_one + num2_pl_one
time.sleep(2)
print('The first player has totally: ', sum_pl_one)
time.sleep(2)

print('Turn of the player', player2)
time.sleep(3)
num1_pl_two = randint(1, 6)
print('It is: ', num1_pl_two)
print('Turn TWO of the player', player2)
time.sleep(3)
num2_pl_two = randint(1, 6)
print('It is: ', num2_pl_two)
sum_pl_two = num1_pl_two + num2_pl_two
print('The second player has totally: ', sum_pl_two)
time.sleep(2)

if sum_pl_one > sum_pl_two:
    print(player1, 'wins. Congratulations!')
elif sum_pl_two > sum_pl_one:
    print(player2, 'wins.Congratulations!')
else:
    print('Tie!!!')