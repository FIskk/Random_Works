#random_name_generator.py

#imports
import random

#Functions

# Generates a random boy or girls name from a pool of 20 each using the
# random module Required input in sex to equal either 'boy' or 'girl'
# and output in 'random_name'
def name_generator(sex):
    number = random.randrange(0, 19)    #Alter this range to account for an increase in names
    if sex == 'boy':
        male_name_list = ['Bob', 'Bill', 'Jim', 'John', 'Sam',
                          'Jake', 'Brandon', 'Tom', 'Rich', 'Karl',
                          'Abel', 'Adam', 'Aaron', 'Brad', 'Brent',
                          'Chuck', 'Chris', 'Cody', 'Collin', 'Max',
                          ]
        random_name = male_name_list[number]
        print("\nYou have been gifted the name", random_name)
    elif sex == 'girl':
        female_name_list = ['Sophia', 'Emma', 'Olivia', 'Ava', 'Isabella',
                            'Mia', 'Zoe', 'Lily', 'Emily', 'Madelyn',
                            'Chloe', 'Charlotte', 'Audrey', 'Avery', 'Abigail',
                            'Harper', 'Hannah', 'Hailey', 'Evelyn', 'Aria'
                            ]
        random_name = female_name_list[number]
        print("\nYou have been gifted the name", random_name)

    return random_name

#name_generator('girl')          #//test code//