# Шеренга. Выведите единственное целое число – номер Пети в шеренге учеников.

from random import randint


def rand_list_students(n):
    list = []
    for i in range(1, n+1):
        list.append(randint(150, 200))
    list.sort(reverse=True)
    return list


def place_in_line(list, growth):
    if list[-1] >= growth:
        return len(list)+1
    else:
        for i in range(len(list)):
            if list[i] <= growth:
                return i+1


try:
    n = int(input('\nEnter number "N" (number of students) from 1 to 100 :\t'))
    growth = int(input("\nEnter Petya's growth from 150 to 200 :\t"))
    if 1 <= n <= 100 and 150 <= growth <= 200:
        list = rand_list_students(n)
        print('\nThe growth of students in the line -->', *list)

        print(
            f"\nPetya's number in the line of students -->\t{place_in_line(list,growth)}\n")
    else:
        print("\nYou must enter number 'N' from 1 to 100, or Petya's growth from 150 to 200, try again!\n")
except ValueError:
    print('\nIncorrect data, you must enter number, try again!\n')
