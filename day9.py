def read_data():
    with open("day9.txt") as f:
        code = f.read().split('\n')
    code = code[:-1]
    code = [int(x) for x in code]
    return code

def check_code(preamble, code):
    ''' Part 1 solution'''
    from itertools import combinations 
   
    for num in range(preamble,len(code)):

        pream = code[num-preamble:num] #separate out the new preamble

        combs = [x + y for (x,y) in combinations(pream, 2)]  #find all combinations of two digits and add them

        if code[num] not in combs:   #check for the next number and see if it is in our list of combined values
            return(code[num])

def find_weakness(invalid, code):
    '''Part 2 solution'''
    for val in range(len(code)):  #step through indexes for start of contiguous segment
        #find all combinations that start with val
        for last in range((val+2),(len(code) + 1)): #step through indexes for end of contiguous segment
            total = sum(code[val:last])
            if total == invalid:    #if we found our number return it
                return(min(code[val:last-1]), max(code[val:last-1]))
            if total > invalid: # total of continous vals is too big
                break  #break the loop and try the next starting value

    

def run_tests():
    code = [35,
            20,
            15,
            25,
            47,
            40,
            62,
            55,
            65,
            95,
            102,
            117,
            150,
            182,
            127,
            219,
            299,
            277,
            309,
            576,
    ]
    preamble = 5
    invalid_num = check_code(preamble, code)
    assert(invalid_num == 127)
    (start, finish) = find_weakness(invalid_num, code)
    assert(start + finish == 62)


def day9():
    code = read_data()
    preamble = 25
    invalid_num = check_code(preamble, code)
    print("Part 1: ", invalid_num)
    (start, finish) = find_weakness(invalid_num, code)
    print("Part 2: ", start + finish)
    
if __name__ == "__main__":
    run_tests()
    day9()