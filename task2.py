# Требуется посчитать сумму целых чисел, расположенных между числами 1 и N включительно.

try:
    n = int(input('\nEnter number "N" from 1 to 10^4 :\t'))
    if 1 <= n <= 10000:
        sum = 0
        for i in range(n+1):
            sum += i
        print(f'\nSum = {sum}\n')
    else:
        print('\nYou must enter number "N" from 1 to 10^4, try again!\n')
except ValueError:
    print('\nIncorrect data, you must enter number, try again!\n')
