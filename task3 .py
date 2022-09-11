# Требуется найти наименьший натуральный делитель целого числа N, отличный от 1.

try:
    n = int(input('\nEnter number "N" from 1 to 10^6 :\t'))
    if 1 <= n <= 1000000:
        divisor = 1
        for i in range(2, n+1):
            if n % i == 0:
                divisor = i
                break
            else:
                divisor = n
        print(f'\nThe smallest natural divisor -->\t{divisor}\n')
    else:
        print('\nYou must enter number "N" from 1 to 10^6, try again!\n')
except ValueError:
    print('\nIncorrect data, you must enter number, try again!\n')
