import numpy as np
import math

def read_data():
    with open("day13.txt") as f:
        notes = f.read().split('\n')
    notes = notes[:-1]
    ourtime = int(notes[0])
    busses = notes[1].replace('x', '-1').split(',')
    busses = [int(x) for x in busses]

    return(ourtime, busses)

def part1(ourtime, busses):
    #now solve the problem
    #take our time, divide by the busses and then round up -- that will give us the next time for each bus
    next_bus = []
    for bus in busses:
        if bus == -1:
            next_bus.append(100000000)
        else:
            next_bus.append(bus * math.ceil(ourtime / bus))
    index_min = np.argmin(next_bus)
    return(busses[index_min] * (next_bus[index_min] - ourtime))

def find_my_code(busses):
    my_code = []
    my_bus = []
    for (ind, bus) in enumerate(busses):
        if bus != -1:
            my_code.append(ind)
            my_bus.append(bus)
    return(my_code, my_bus)

def part2(busses):

    (my_code, my_bus) = find_my_code(busses)

    #we start off knowing that we'll have to step in chunks of time equal to the first bus's loop
    step = my_bus[0]
    time = 0

    #now we step through the rest of the buses and find their associated factors
    for (code, bus) in zip(my_code[1:], my_bus[1:]):
        while (time + code) % bus != 0:
            time+=step
        #the above while loop finishes when we find the step size for bus n, so we increment our step size by that
        step *= bus
    return(time)


def run_tests():
    '''run the main test case (floor_plan_list) and the mini test cases given to us in the question'''

    notes = [
        '939',
        '7,13,x,x,59,x,31,19'
    ]
    ourtime = int(notes[0])
    busses = notes[1].replace('x', '-1').split(',')
    busses = [int(x) for x in busses]
    assert (part1(ourtime, busses) == 295)
    assert(part2(busses) == 1068781)


    notes = [
        '939',
        '17,x,13,19'
    ]
    ourtime = int(notes[0])
    busses = notes[1].replace('x', '-1').split(',')
    busses = [int(x) for x in busses]
    assert(part2(busses) == 3417)
    return
    notes = [
        '939',
        '67,7,59,61'
    ]
    ourtime = int(notes[0])
    busses = notes[1].replace('x', '-1').split(',')
    busses = [int(x) for x in busses]
    assert(part2(busses) == 754018)

    notes = [
        '939',
        '67,x,7,59,61'
    ]
    ourtime = int(notes[0])
    busses = notes[1].replace('x', '-1').split(',')
    busses = [int(x) for x in busses]
    assert(part2(busses) == 779210)  

    notes = [
        '939',
        '67,7,x,59,61'
    ]
    ourtime = int(notes[0])
    busses = notes[1].replace('x', '-1').split(',')
    busses = [int(x) for x in busses]
    assert(part2(busses) == 1261476)    

    notes = [
        '939',
        '1789,37,47,1889'
    ]
    ourtime = int(notes[0])
    busses = notes[1].replace('x', '-1').split(',')
    busses = [int(x) for x in busses]
    assert(part2(busses) == 1202161486)


def day11():
    (ourtime, busses) = read_data()

    print("Part 1", part1(ourtime, busses))
    print("Part 2", part2(busses))  


##########Failed attempts -- these work on the test inputs but way too slow for the real problem ######################

def part2_tooslow(busses):
    step = -1
    while True:
        answer = True
        step+=1
        ourtime = step * busses[0]
        #print("time stamp", ourtime)

        for (ind, bus) in enumerate(busses[1:]):
#            print("bus number", bus)
            if bus == -1:
                pass
            else:
                if bus * math.ceil(ourtime / bus) != ourtime + ind+1:
                    answer = False
#                    print("no good", bus)
                    pass
#                elif bus in [13, 17, 29, 677, 37, 19]:
#                    print('good bus', bus)
        if answer == True:
            return(ourtime)


def part2_sloooooow(busses):

    (my_code, my_bus) = find_my_code(busses)
    print("my code", my_code)
    print("my_bus", my_bus)

    step = -1
    
    while True:
        answer = True
        step+=1
        ourtime = step * my_bus[0]
        #print out steps now and then to make sure things are still running
        if step % 1000000 == 0:
            print("time stamp", ourtime)

        for (code, bus) in zip(my_code, my_bus):
#            print("code, bus number", code, bus)
#            print("left, right", bus * math.ceil(ourtime / bus), ourtime + code+1)
            if bus * math.ceil(ourtime / bus) != ourtime + code+1:
                answer = False
#                print("no good", bus)
#                    pass
#            elif bus in [13, 17, 29, 677, 37, 19]:
#                print('good bus', bus)
        if answer == True:
            return(ourtime)

def part2_fasterbutnotenough(busses):

    (my_code, my_bus) = find_my_code(busses)
    print("my code", my_code)
    print("my_bus", my_bus)

    step = -1
    
    while True:
        answer = True
        step+=1
        ourtime = step * my_bus[0]
        #print out steps now and then to make sure things are still running
        if step % 1000000 == 0:
           print("time stamp", ourtime)


        for (code, bus) in zip(my_code[1:], my_bus[1:]):

            if (ourtime + code) % bus != 0:
                answer = False
                break
        if answer == True:
            print('ourtime', ourtime)
            return(ourtime)


if __name__ == "__main__":
    run_tests()
    day11()