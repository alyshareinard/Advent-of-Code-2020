import numpy as np

def read_data():
    with open("day18.txt") as f:
        calcs = f.read().split('\n')
    return calcs[0:-1]

def eval_segment_afirst(calc):
    answer = 0
    ind = 0
    eqn = calc.split(' ')

    #first look for adds
    eqn2 = []
    while len(eqn)>=3:
        num1 = int(eqn[0])
        op = eqn[1]
        num2 = int(eqn[2])
        if op == '+':
            ans = num1 + num2
            eqn = [ans] + eqn[3:]
        else: 
            eqn2.append(num1)
            eqn2.append(op)
            eqn = eqn[2:]

    eqn2 = eqn2 + eqn
    if len(eqn2) == 1:
        return(eqn2[0])

    while True:
        num1 = int(eqn2[0])
        op = eqn2[1]
        num2 = int(eqn2[2])

        if op == '*':
            ans = num1 * num2
        elif op == '+':
            ans = num1 + num2
        if len(eqn2) == 3: 
            return(ans)
        else:
            eqn2 = [ans] + eqn2[3:]


def eval_segment(calc):
    answer = 0
    ind = 0
    eqn = calc.split(' ')
    while True:
        num1 = int(eqn[0])
        op = eqn[1]
        num2 = int(eqn[2])

        if op == '*':
            ans = num1 * num2
        elif op == '+':
            ans = num1 + num2
        if len(eqn) == 3: 
            return(ans)
        else:
            eqn = [ans] + eqn[3:]

def parse_calc(calc, add_first = False):
    #first deal with parenthesis
    while True:
        #find first ')'
        start_paren = 0
        if calc.count(')') == 0:
            if add_first:
                return(eval_segment_afirst(calc))
            else:
                return(eval_segment(calc))
        for (ind, char) in enumerate(calc):
            if char == '(':
                start_paren =  ind
            elif char == ')':
                if add_first:
                    seg_ans = eval_segment_afirst(calc[start_paren + 1:ind])
                else:  
                    seg_ans = eval_segment(calc[start_paren + 1:ind])  
                calc = calc[:start_paren] + str(seg_ans) + calc[ind+1:]

                break


def find_sum(calcs, add_first=False):
    solns = []
    for calc in calcs:
        return_val = parse_calc(calc, add_first)
        solns.append(return_val)


    return(sum(solns))


def run_tests():
    calcs = [
            '1 + 2 * 3 + 4 * 5 + 6',
            '1 + (2 * 3) + (4 * (5 + 6))',
            '2 * 3 + (4 * 5)',
            '5 + (8 * 3 + 9 + 3 * 4 * 3)',
            '5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))',
            '((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2',
    ]

    assert(find_sum(calcs) == 26457)
    print("\n\n")
    
    print(find_sum(calcs, add_first = True))

   
def day18():
    calcs = read_data()

    print("Part 1: ", find_sum(calcs))
    print("Part 2: ", find_sum(calcs, add_first = True))


if __name__ == "__main__":
    run_tests()
    day18()