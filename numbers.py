number = int(input('Enter a number'))
last = number % 10
max_num = last
last_num = 1
position = 1
number = number // 10
while number > 0:
    position += 1
    last = number % 10
    if last > max_num:
        max_num = last
        last_num = position
    number = number // 10
print('Max number is', max_num, ' and it"s point number is', last_num)