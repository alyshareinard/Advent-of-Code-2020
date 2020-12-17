import numpy as np
import math

def read_data():

    numbers = [0,14,1,3,7,9]
    return(numbers)


def update_numbers(numbers_dict):
    for key, val in numbers_dict.items():
        numbers_dict[key]=val+1

    return(numbers_dict)
    
def play_game(numbers, stop):
    count = 0

    #set up dictionary with the given numbers
    numbers_dict = {}
    for val, key in enumerate(numbers[0:-1]):
        numbers_dict[key]=val+1
        
    step = len(numbers)

    last_number = numbers[-1]

    #now step through the game
    while step < stop:
        if step % 1000000 == 0:
            print(step/1000000, "of 30")

        #if we've already said the number, we look up the last turn it was spoken
        #subtract from this turn to give the next number, 
        #then reset the dictionary element for the number to indicate it was spoken this turn.  
        if last_number in numbers_dict.keys():
            temp = step - numbers_dict[last_number]

            numbers_dict[last_number]=step
            last_number = temp
        #if the number is a new one, we set it's "last used" to this turn and set the next number as 0
        else:
            numbers_dict[last_number]=step
            last_number = 0
        step+=1
    return(last_number)


def run_tests():
    numbers = [
        0,3,6
    ]

    
    assert(play_game(numbers, 2020) == 436)

    numbers = [
        1,3,2
    ]
    
    assert(play_game(numbers, 2020) == 1)

    numbers = [
        2, 1, 3
    ]
    
    assert(play_game(numbers, 2020) == 10)

    numbers = [
        1,2,3
    ]
    
    assert(play_game(numbers, 2020) == 27)

    numbers = [
        2, 3, 1
    ]
    
    assert(play_game(numbers, 2020) == 78)

    numbers = [
        3,2,1
    ]
    
    assert(play_game(numbers, 2020) == 438)

    numbers = [
        3,1,2
    ]
    
    assert(play_game(numbers, 2020) == 1836)


def day15():
    numbers = read_data()

    print("Part 1", play_game(numbers, 2020))
    print("Part 2", play_game(numbers, 30000000))  



if __name__ == "__main__":
    run_tests()
    day15()