#Dice_Roller.py

#imports

import random


#Functions


def random_num_generator(num_of_sides, num_of_dice):      #Generates the random numbers based on the input from the user and returns the numbers in a list called 'list_of_numbers'
    list_of_numbers = []
    generate = 1
    while generate <= num_of_dice:
        random_number = random.randrange(1, num_of_sides)
        list_of_numbers.append(random_number)
        generate += 1

    return list_of_numbers


def dice_roller():      #Gets the number of dice and sides from the user. Then calls the number generator and outputs the numbers.
    roll = 0
    while roll == 0:
        num_of_dice = int(input("\nHow many dice would you like to roll (ex: 1, 5, 8)? \n"))
        num_of_sides = int(input("How many side do these dice have (ex: 1, 5, 8)? \n")) + 1

        answer = random_num_generator(num_of_sides, num_of_dice)
        print("\nyour rolls were", answer, "\n")
        break


#Body

go = 0
while go == 0:                      #Starts the program
    start = input("Would you like to roll some dice (yes, no)? ")
    lower_start = start.lower()
    if lower_start.isalpha() is True and lower_start == 'yes':
        dice_roller()
        break
    elif lower_start.isalpha() is True and lower_start == 'no':
        print("OK, have a nice day.")
        exit()
    else:
        print("Please enter yes or no.")


again = 0
while again == 0:               #After the first run prompts the user to roll again
    play_again = str(input("Would you like to roll again (yes, no)? "))
    lower_play_again = play_again.lower()
    if lower_play_again.isalpha() is True and lower_play_again == 'yes':
        dice_roller()
    elif lower_play_again.isalpha() is True and lower_play_again == 'no':
        print("OK, have a nice day.")
        exit()
    else:
        print("Please enter yes or no.")