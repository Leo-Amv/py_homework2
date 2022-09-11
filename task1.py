# На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом. (1 или 0)
# Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были повернуты вверх одной и той же стороной.

from random import randint


def rand_list_coins(n):
    list = []
    for i in range(1, n+1):
        list.append(randint(0, 1))
    return list


def count_flipped_coins(list):
    count0 = 0
    count1 = 0
    for i in range(len(list)):
        if list[i] == 0:
            count0 += 1
        else:
            count1 += 1
    if count0 <= count1:
        return count0
    else:
        return count1


try:
    n = int(input('\nEnter number "N" (the number of coins) from 1 to 100 :\t'))
    if 1 <= n <= 100:
        list = rand_list_coins(n)
        count = count_flipped_coins(list)
        print('\nReceived coins -->\t', *list)
        print(f'\nCount of flipped coins -->  {count}\n')
    else:
        print('\nYou must enter number "N" from 1 to 100, try again!\n')
except ValueError:
    print('\nIncorrect data, you must enter number, try again!\n')
