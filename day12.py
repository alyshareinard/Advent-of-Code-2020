def read_data():
    with open("day12.txt") as f:
        directions = f.read().split('\n')
    
    return directions[:-1]


def follow_waypoint(directions):

    NSship = 0
    EWship = 0
    NSway = 1
    EWway = 10

    for direction in directions:
        inst = direction[0]
        val = int(direction[1:])
        if inst == 'N':
            NSway += val
        elif inst == 'S': 
            NSway -= val
        elif inst == 'E':
            EWway += val
        elif inst == 'W':
            EWway -= val
        elif inst == 'L':  
            if val == 270:
                NSway, EWway = -EWway, NSway
            elif val == 180:
                NSway, EWway = -NSway, -EWway
            elif val == 90:
                NSway, EWway = EWway, -NSway
        elif inst == 'R':  
            if val == 90:
                NSway, EWway = -EWway, NSway
            elif val == 180:
                NSway, EWway = -NSway, -EWway
            elif val == 270:
                NSway, EWway = EWway, -NSway
        elif inst == 'F': 
            EWship += EWway * val
            NSship += NSway * val

    return(abs(EWship)+ abs(NSship))

def follow_directions(directions):
    NSval = 0
    EWval = 0
    facing = 90

    for direction in directions:
        inst = direction[0]
        val = int(direction[1:])
        if inst == 'N':
            NSval += val
        elif inst == 'S': 
            NSval -= val
        elif inst == 'E':
            EWval += val
        elif inst == 'W':
            EWval -= val
        elif inst == 'L':
            facing -= val
            facing = facing % 360
        elif inst == 'R':
            facing += val
            facing = facing % 360
        elif inst == 'F':
            #let's assume facing will always be one of N/S/E/W
            if facing == 0:
                NSval += val
            elif facing == 90:
                EWval += val
            elif facing == 180:
                NSval -= val
            elif facing == 270:
                EWval -= val
    return(abs(EWval) + abs(NSval))
        
        

def run_tests():
    directions = [
        'F10',
        'N3',
        'F7',
        'R90',
        'F11',
    ]
    assert(follow_directions(directions) == 25)
    assert(follow_waypoint(directions) == 286)
    

   
def day10():
    directions = read_data()
    print("Part 1: ", follow_directions(directions))
    print("Part 2: ", follow_waypoint(directions))

    
if __name__ == "__main__":
    run_tests()
    day10()