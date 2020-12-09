def read_data():
    with open("day8.txt") as f:
        forms_db = f.read().split('\n')
    return forms_db

def run_instructions1(instructions):
    index = 0
    accum = 0
    last_instr = False
    ind_visited = []
    while True:
        if index == len(instructions):
            
            last_instr = True
            return(accum, ind_visited, last_instr)
        #parse next instruction
        (inst, val) = instructions[index].split(' ')
        val = int(val)
        if index in ind_visited:
            return(accum, ind_visited, last_instr)
          

        ind_visited.append(index)
        if inst == 'acc':
            accum += val
            index+=1
        elif inst == 'jmp':
            index += val
        else:
            index+=1
        
def find_corrupt(ind_visited, instructions):

    for ind in ind_visited[::-1]:
        new_instructions = [x for x in instructions]
        old_inst = new_instructions[ind].split(' ')
        if old_inst[0] == 'jmp':
            new_inst = 'nop '+old_inst[1]
            new_instructions[ind]= new_inst
            (accum, _, done) = run_instructions1(new_instructions)
            if done:
                return(accum)
        elif old_inst[0] == 'nop':
            new_inst = 'jmp '+old_inst[1]
            new_instructions[ind]= new_inst
            (accum, _, done) = run_instructions1(new_instructions)
            if done:
                return(accum)
        


def run_tests():
    instructions = [
        'nop +0',
        'acc +1',
        'jmp +4',
        'acc +3',
        'jmp -3',
        'acc -99',
        'acc +1',
        'jmp -4',
        'acc +6',
    ]
    (accum, ind_visited, _) = run_instructions1(instructions)

    assert(accum == 5)
    accum = find_corrupt(ind_visited, instructions)
    print("part 2 test", accum)


        

def day8():
    instructions = read_data()
    (accum, ind_visited, _) = run_instructions1(instructions)
    print("Part 1: ", accum)

    accum = find_corrupt(ind_visited, instructions)
    print("Part 2: ", accum)

    
if __name__ == "__main__":
    run_tests()
    day8()