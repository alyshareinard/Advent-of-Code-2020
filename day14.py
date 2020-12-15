def read_data():
    with open("day14.txt") as f:
        directions = f.read().split('\n')
    
    return directions[:-1]


def apply_mask(val, mask):
    val = str(val)
    for ind, mval in enumerate(mask):
        if mask[ind] != 'X':
            val = val[0:ind] + mask[ind] + val[ind+1:]

    return(val)


def parse_program(program):
    values = {}
    for line in program:
        line = line.split(' = ')

        if line[0]=='mask':
            mask = line[1]

        elif line[0][0:3] == 'mem':
        
            loc = line[0][4:-1]
            val = f'{int(line[1]):036b}'

            #Now apply the mask
            values[loc] = int(apply_mask(val, mask), 2)

    return(sum(values.values()))

def apply_mask_v2(val, mask):
    val = [str(val)]
    for ind in range(len(mask)):

        if mask[ind] == '1':
            for i in range(len(val)):

                val[i] = val[i][0:ind] + mask[ind] + val[i][ind+1:]

        elif mask[ind] == 'X':
            for i in range(len(val)):
                val[i] = val[i][0:ind] + '0' + val[i][ind+1:]
                val.append(val[i][0:ind] + '1' + val[i][ind+1:])
            
    return(val)

def parse_program_v2(program):
    values = {}
    for line in program:
        line = line.split(' = ')
        if line[0]=='mask':
            mask = line[1]

        elif line[0][0:3] == 'mem':
        
            val = int(line[1])
            loc = f'{int(line[0][4:-1]):036b}'

            #Now apply the mask
            locs = apply_mask_v2(loc, mask)
            locs = [int(x, 2) for x in locs]
            for loc in locs:
                values[loc] = val

    return(sum(values.values()))

def run_tests():
    program = [
        'mask = XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X',
        'mem[8] = 11',
        'mem[7] = 101',
        'mem[8] = 0',
    ]
    assert(parse_program(program) == 165)

    program = [
        'mask = 000000000000000000000000000000X1001X',
        'mem[42] = 100',
        'mask = 00000000000000000000000000000000X0XX',
        'mem[26] = 1',
    ]
    assert(parse_program_v2(program) == 208)
    

   
def day14():
    program = read_data()
    print("Part 1: ", parse_program(program))
    print("Part 2: ", parse_program_v2(program))   

    
if __name__ == "__main__":
    run_tests()
    day14()