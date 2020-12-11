def read_data():
    with open("day10.txt") as f:
        adaptors_db = f.read().split('\n')
    adaptors_db = adaptors_db[:-1]
    adaptors_db = [int(x) for x in adaptors_db]
    return adaptors_db


def adaptor_combs(adaptors):
    adaptors.append(0)
    adaptors.append(max(adaptors)+3)
    adaptors.sort()
    diffs = []

    for i in range(1, len(adaptors)):
        diffs.append(adaptors[i] - adaptors[i-1])

    threes = diffs.count(3)
    ones = diffs.count(1)
    return(threes*ones)

def figure_out_combos():
    comb_dict={}
    from itertools import combinations
    for i in range(15):  #let's start with 15 1s in a row -- we can increase this later if we need to.  
        my_list = list(range(1, i+2))  #set up our list
        my_combs = []                   #have an empty list for the combinations
        for x in range(1, i+1):         #step through the length and find combionations of length 1, 2, ... i+1
            my_combs += list(combinations(my_list, x))  #add all these combiations to a list of lists
        good_combs=[]
        for comb in my_combs:               #now we step through our list of lists
            full_comb = [0] + list(comb) + [my_list[-1]+3]          #add on the initial and final adaptors
            diff = [full_comb[x]-full_comb[x-1] for x in range(1, len(full_comb))]      #find the differences in voltages between each consequetive adaptor
            if all(x<=3 for x in diff):  # only add the ones that have no jumps that are more than 3
                good_combs.append(comb)
        comb_dict[i+1]=len(good_combs)+1  #take the length of the good combinations and add that to my lookup table
    return(comb_dict)
        

def sort_adaptors(adaptors):
    adaptors.append(0)
    adaptors.append(max(adaptors)+3)
    adaptors.sort()
    diffs = []
    for i in range(1, len(adaptors)):
        diffs.append(adaptors[i] - adaptors[i-1])
    return(diffs)

def part1(diffs):
    threes = diffs.count(3)
    ones = diffs.count(1)
    return(threes*ones)

def part2(diffs):
    comb_dict = figure_out_combos()
    combinations = 1
    index = -1
    ones_count = 0
    #now we use our dictionary of 1s to simplify things 
    #we step through our adaptors (rather the voltage differences between adaptors) and just count up the 1s
    #when we hit a 3 we use check our dictionary to see how many combinations correspond that that number of
    #1s.  Then we zero out our ones count and continue.  
    while index < len(diffs)-1:  
        index+=1

        if diffs[index]==1:

            ones_count+=1
        elif diffs[index]==3:

            if ones_count > 0:
                try:
                    combinations *= comb_dict[ones_count]
                except:
                    print('too many ones', ones_count) #this would indicate we should extend the loop in comb_dict -- never happens
            ones_count=0
        else:  #a check just in case some differences are not in 1 or 3 -- never happens
            print("problem -- index, adaptor[index]", index, diffs[index])
    return(combinations)


def run_tests():
    adaptors = [
        16,
        10,
        15,
        5,
        1,
        11,
        7,
        19,
        6,
        12,
        4,
    ]

    diffs = sort_adaptors(adaptors)

    part1_ans= part1(diffs)
    assert(part1_ans == 35)

    part2_ans = part2(diffs)
    assert(part2_ans == 8)

    adaptors = [
        28,
        33,
        18,
        42,
        31,
        14,
        46,
        20,
        48,
        47,
        24,
        23,
        49,
        45,
        19,
        38,
        39,
        11,
        1,
        32,
        25,
        35, 
        8,
        17,
        7,
        9,
        4,
        2,
        34,
        10,
        3,
    ]
    diffs = sort_adaptors(adaptors)

    part1_ans= part1(diffs)
    assert(part1_ans == 220)

    part2_ans = part2(diffs)
    assert(part2_ans == 19208)



def day10():
    adaptors = read_data()

    diffs = sort_adaptors(adaptors)

    part1_ans= part1(diffs)
    print("Part 1: ", part1_ans)

    part2_ans = part2(diffs)
    print("Part 2: ", part2_ans)

    
if __name__ == "__main__":
    figure_out_combos()
    run_tests()
    day10()