import numpy as np

def read_data():
    with open("day17.txt") as f:
        cubes = f.read().split('\n')
    cubes= cubes[:-1]
    return cubes


def create_array(cubes):
    ''' separate out the lines and characters, then turn into an np.array'''
    new_plan = []
    for line in cubes:
        sep_line = []
        for char in line:
            sep_line.append(char) 
        new_plan.append(sep_line)
    new_plan = np.array(new_plan)
    return np.expand_dims(new_plan, axis=0)

def create_array_4d(cubes):
    ''' separate out the lines and characters, then turn into an np.array'''
    new_plan = []
    for line in cubes:
        sep_line = []
        for char in line:
            sep_line.append(char) 
        new_plan.append(sep_line)
    new_plan = np.array(new_plan)
    return np.expand_dims(np.expand_dims(new_plan, axis=0), axis=0)


def check_cube(small_area):
    small_area = list(small_area.flatten())
    cube = small_area[13]

    surrounding = small_area[:13] + small_area[14:] #exclude the seat itself

    occupied = surrounding.count('#')

    if cube == '#':
        if (occupied == 2 or occupied == 3):
            cube = '#'
        else:
            cube = '.'
    elif cube == '.' and occupied ==3:
        cube = '#'

    return cube 

def check_cube_4D(small_area):
    small_area = list(small_area.flatten())
    cube = small_area[40]

    surrounding = small_area[:40] + small_area[41:] #exclude the seat itself

    occupied = surrounding.count('#')


    if cube == '#':
        if (occupied == 2 or occupied == 3):
            cube = '#'
        else:
            cube = '.'
    elif cube == '.' and occupied ==3:
        cube = '#'

    return cube 

def check_map(cubes):
    #first add a border
    cubes = np.pad(cubes, pad_width=2, mode='constant', constant_values='.')
    new_cubes=[]
    #now go through each seat and check the surrounding seats
    for i in range(1, len(cubes)-1):
 #       print("i",i)
        new_row = []
        for j in range(1, len(cubes[0])-1):
#            print("j", j)
            new_cube= []
            for k in range(1, len(cubes[0][0])-1):
 #               print("k", k)
                new_cube.append(check_cube(cubes[i-1:i+2, j-1:j+2, k-1:k+2]))
            new_row.append(new_cube)
        new_cubes.append(new_row)
    return np.array(new_cubes)

def check_map_4D(cubes):
    #first add a border
    cubes = np.pad(cubes, pad_width=2, mode='constant', constant_values='.')
    new_cubes=[]
    #now go through each seat and check the surrounding seats
    for i in range(1, len(cubes)-1):
 #       print("i",i)
        new_row = []
        for j in range(1, len(cubes[0])-1):
#            print("j", j)
            new_cube= []
            for k in range(1, len(cubes[0][0])-1):
 #               print("k", k)
                new_hyper = []
                for w in range(1, len(cubes[0][0][0])-1):
                    new_hyper.append(check_cube_4D(cubes[i-1:i+2, j-1:j+2, k-1:k+2, w-1:w+2]))
                new_cube.append(new_hyper)
            new_row.append(new_cube)
        new_cubes.append(new_row)
    return np.array(new_cubes)

def trim_edges(cubes):
#    print("shape before", cubes.shape)
    if (cubes[0, :, :] == "#").sum() == 0:
        cubes = cubes[1:, :, :]
    if (cubes[-1, :, :] == "#").sum() == 0:
        cubes = cubes[:-1, :, :]
    if (cubes[:, 0, :] == "#").sum() == 0:
        cubes = cubes[:, 1:, :]
    if (cubes[:, -1, :] == "#").sum() == 0:
        cubes = cubes[:, :-1, :]
    if (cubes[:, :, 0] == "#").sum() == 0:
        cubes = cubes[:, :, 1:]
    if (cubes[:, :, -1] == "#").sum() == 0:
        cubes = cubes[:, :, :-1]
#    print("shape after", cubes.shape)
    return(cubes)

def trim_edges_4D(cubes):
#    print("shape before", cubes.shape)
    if (cubes[0, :, :, :] == "#").sum() == 0:
        cubes = cubes[1:, :, :, :]
    if (cubes[-1, :, :, :] == "#").sum() == 0:
        cubes = cubes[:-1, :, :, :]
    if (cubes[:, 0, :, :] == "#").sum() == 0:
        cubes = cubes[:, 1:, :, :]
    if (cubes[:, -1, :, :] == "#").sum() == 0:
        cubes = cubes[:, :-1, :, :]
    if (cubes[:, :, 0, :] == "#").sum() == 0:
        cubes = cubes[:, :, 1:, :]
    if (cubes[:, :, -1, :] == "#").sum() == 0:
        cubes = cubes[:, :, :-1, :]
    if (cubes[:, :, :, 0] == "#").sum() == 0:
        cubes = cubes[:, :, :, 1:]
    if (cubes[:, :, :, -1] == "#").sum() == 0:
        cubes = cubes[:, :, :, :-1]
#    print("shape after", cubes.shape)
    return(cubes)

def run_simulation(cubes, cycles):
    for _ in range(cycles):

        cubes = check_map(cubes)
        cubes = trim_edges(cubes)
    return((cubes == "#").sum())

def run_simulation_4d(cubes, cycles):
    for _ in range(cycles):

        cubes = check_map_4D(cubes)
        cubes = trim_edges_4D(cubes)

    return((cubes == "#").sum())

def run_tests():
 
    cubes_init= [
        '.#.',
        '..#',
        '###',
    ]

    cubes = create_array(cubes_init)
    cycles = 6
    assert(run_simulation(cubes, cycles) == 112)
    cubes = create_array_4d(cubes_init)
    assert(run_simulation_4d(cubes, cycles) == 848 )

def day17():
    cubes_init = read_data()
    cubes = create_array(cubes_init)
    cycles = 6
    print("Part 1:", run_simulation(cubes, cycles))

    cubes=create_array_4d(cubes_init)
    print("Part 2:", run_simulation_4d(cubes, cycles))
    
if __name__ == "__main__":
    run_tests()
    day17()