import numpy as np

def read_data():
    with open("day11.txt") as f:
        floor_plan = f.read().split('\n')
    floor_plan = floor_plan[:-1]
    return floor_plan

def create_array(floor_plan):
    ''' separate out the lines and characters, then turn into an np.array'''
    new_plan = []
    for line in floor_plan:
        sep_line = []
        for char in line:
            sep_line.append(char) 
        new_plan.append(sep_line)
    new_plan = np.array(new_plan)
    return new_plan


def run_tests():
    '''run the main test case (floor_plan_list) and the mini test cases given to us in the question'''

    floor_plan_list = [
        '#.##.##.##',
        '#######.##',
        '#.#.#..#..',
        '####.##.##',
        '#.##.##.##',
        '#.#####.##',
        '..#.#.....',
        '##########',
        '#.######.#',
        '#.#####.##',
    ]
    floor_plan = create_array(floor_plan_list)

    floor_plan = find_equilibrium(floor_plan)

    assert((floor_plan == '#').sum() == 37)

    mini_test_list = [
        '.......#.',
        '...#.....',
        '.#.......',
        '.........',
        '..#L....#',
        '....#....',
        '.........',
        '#........',
        '...#.....',

        ]

    mini_test = create_array(mini_test_list)
    assert(seat_los(mini_test, 4, 3, return_count=True)==8)

    mini_test_list = [
        '.............',
        '.L.L.#.#.#.#.',
        '.............',
        ]

    mini_test = create_array(mini_test_list)

    assert(seat_los(mini_test, 1, 1, return_count=True)==0)


    mini_test_list = [
        '.##.##.',
        '#.#.#.#',
        '##...##',
        '...L...',
        '##...##',
        '#.#.#.#',
        '.##.##.',
        ]

    mini_test = create_array(mini_test_list)

    assert(seat_los(mini_test, 3, 3, return_count=True)==0)

    floor_plan = create_array(floor_plan_list)
    floor_plan = find_equilibrium2(floor_plan)
    assert((floor_plan == '#').sum() == 26)

def find_equilibrium(floor_plan):
    ''' rerun the seating (check_map) arrangement until it stops changing'''
    old_floor_plan = list(floor_plan.flatten()) #use 'list' to avoid creaing a pointer to same array

    while True:
        floor_plan = check_map(floor_plan)
#        print(floor_plan)    
        if list(floor_plan.flatten()) == old_floor_plan:
            return floor_plan
        old_floor_plan = list(floor_plan.flatten())

def find_equilibrium2(floor_plan):
    '''rerun the line of site (check_los) seating arrangement until it stops changing'''
    old_floor_plan = list(floor_plan.flatten())

    while True:
        floor_plan = check_los(floor_plan)   
        if list(floor_plan.flatten()) == old_floor_plan:
            return floor_plan
        old_floor_plan = list(floor_plan.flatten())


def check_seat(small_area):
    small_area = list(small_area.flatten())
    seat = small_area[4]
    surrounding = small_area[:4] + small_area[5:] #exclude the seat itself
    occupied = surrounding.count('#')

    if seat == 'L' and occupied == 0:
        seat = '#'
    elif seat == '#' and occupied >= 4:
        seat = 'L'
    return seat #note -- if seat == '.' is handled trivially -- it doesn't enter the if statements and is just returned as is



def next_seat(val):
    cont = True
    occup = 0
    if val == '#':
        occup= 1
        cont = False
    elif val == 'L':
        cont = False
    return(occup, cont)

def seat_los(floor_plan, i, j, return_count=False):
    count = 0
    myseat= floor_plan[i, j]
    if myseat == '.':
        return('.')

    #set up ranges of indexes to check in all directions
    i_down = range(i-1, -1, -1)
    i_up = range(i+1, len(floor_plan))
    j_down = range(j-1, -1, -1)
    j_up = range(j+1, len(floor_plan[0]))
    for ii in i_down:
        (occup, cont) = next_seat(floor_plan[ii, j])
        count += occup
        if not cont:
            break

    for ii in i_up:
        (occup, cont) = next_seat(floor_plan[ii, j])
        count += occup
        if not cont:
            break

    for jj in j_down:
        (occup, cont) = next_seat(floor_plan[i, jj])
        count += occup
        if not cont:
            break

    for jj in j_up:
        (occup, cont) = next_seat(floor_plan[i, jj])
        count += occup
        if not cont:
            break

    #now the 4 diagonals
    for ii, jj in zip(i_up, j_up):
        (occup, cont) = next_seat(floor_plan[ii, jj])
        count += occup
        if not cont:
            break

    for ii, jj in zip(i_down, j_up):
        (occup, cont) = next_seat(floor_plan[ii, jj])
        count += occup
        if not cont:
            break

    for ii, jj in zip(i_up, j_down):
        (occup, cont) = next_seat(floor_plan[ii, jj])
        count += occup
        if not cont:
            break

    for ii, jj in zip(i_down, j_down):
        (occup, cont) = next_seat(floor_plan[ii, jj])
        count += occup
        if not cont:
            break

    if return_count:
        return(count)

    if myseat == '#' and count >=5:
        return('L')
    elif myseat == 'L' and count == 0:
        return('#')
    else: 
        return(myseat)

def check_map(floor_plan):
    #first add a border of floor
    floor_plan = np.pad(floor_plan, pad_width=1, mode='constant', constant_values='.')
    new_plan=[]
    #now go through each seat and check the surrounding seats
    for i in range(1, len(floor_plan)-1):
        new_row = []
        for j in range(1, len(floor_plan[0])-1):
            new_row.append(check_seat(floor_plan[i-1:i+2, j-1:j+2]))
        new_plan.append(new_row)
    return np.array(new_plan)

def check_los(floor_plan):
    #first add a border of floor
    floor_plan = np.pad(floor_plan, pad_width=1, mode='constant', constant_values='.')
    new_plan=[]
    for i in range(1, len(floor_plan)-1):
        new_row = []
        for j in range(1, len(floor_plan[0])-1):
            new_row.append(seat_los(floor_plan, i, j))
        new_plan.append(new_row)
    return np.array(new_plan)


def day11():
    floor_plan_list = read_data()
    floor_plan = create_array(floor_plan_list)

    floor_plan = find_equilibrium(floor_plan)
    print("Part 1:", (floor_plan == '#').sum())

    floor_plan = create_array(floor_plan_list)
    floor_plan = find_equilibrium2(floor_plan)
    print("Part 2:", (floor_plan == '#').sum())
    
if __name__ == "__main__":
    run_tests()
    day11()