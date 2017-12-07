#Opening_functions.py

#The main file

#Imports
import random_name_generator

#Functions


def opening_screen():           #The Title message at startup
    print("\t\tWELCOME TO THE WORLD!")
    print("\t    -this is my first game, enjoy-")
    input("\tPress ENTER to move to the next screen")


def personal_info():            #Acquire player information
    sex = ''
    while sex != 'boy' and sex != 'girl':
        sex = str(input("\nAre you a boy or a girl\n >>> "))
        sex = sex.lower()
    name_input = str(input("\nPlease enter your name or what you would like to be called\n"
                     "If you would like to have a name chosen for you just press ENTER \n >>> "))
    if name_input is '':
        name = random_name_generator.name_generator(sex)
    else:
        name = name_input

    return sex, name


def greeting(player):           #Opening
    input("Good day " + player_info[1] + ", press ENTER to begin\n")

#Body
#sex = 'boy'                #test code

#random_name_generator.name_generator(sex)          #test code

opening_screen()


global_sex, global_name = personal_info()

#print("His/Her name is", global_name, "and he/she is a", global_sex)   #Test Code

player_info = [global_sex, global_name]   #The players information 0 = sex, 1 = name

#print(player_info)                 #test code

greeting(player_info[1])
