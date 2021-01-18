import numpy as np
import math

def read_data(filename):
    with open(filename) as f:
        rules_messages = f.read().split('\n\n')
    rules = rules_messages[0].split("\n")
    messages = rules_messages[1].split("\n")
    return (rules, messages)

def reduce_ors(rule):
    rule1 = []
    rule2 = []

    first = True
    for item in rule:

        if '|' in item  and item != '|' and first == True:
            split = item.index('|')

            rule1 = rule1 + item[:split]
            rule2 = rule2 + item[split+1:]
            first = False
        else:
            rule1.append(item)
            rule2.append(item)

    return(rule1, rule2)


def isdone(rule):
    for item in rule:
        if type(item) == list:
            return False
        if not item.isalpha():
            return False
    return True


def process_rule(rule, rule_dict):
    from itertools import chain
    if '|' in chain(*rule):
        (rule1, rule2) = reduce_ors(rule)
        return([rule1, rule2])
    else:
        new_rule = []
        for item in rule:
            if item.isnumeric(): 
                insert = rule_dict[item]
                if '|' in insert or type(insert) == str:
                    new_rule.append(rule_dict[item])
                else:
                    new_rule = new_rule + rule_dict[item]

            else:
                new_rule.append(item)
        return([new_rule])


def make_rulesdict(rules):
    rule_dict={}

    for rule in rules:
        num, definition = rule.split(': ')
        if '"' in definition:
            rule_dict[num] = definition.replace('"', '')
        else:
            rule_dict[num] = definition.split(' ')
    return(rule_dict)

def create_combinations(rule_dict, first_rule = '0'):

    from collections import deque

    rules = deque()
    if '|' in rule_dict[first_rule]:
        rules.append([rule_dict[first_rule]])
    else:
        rules.append(rule_dict[first_rule])

    done = [] #will hold all combinations that have been played out
    while len(rules)>0:
        rule = rules.pop()

        new_rules = process_rule(rule, rule_dict)
        for new_rule in new_rules:
            if isdone(new_rule):# and new_rule not in done:
                done.append(''.join(new_rule))
            else:
                rules.insert(0, new_rule)

    return done


def part1(filename):
    (rules, messages) = read_data(filename)

    rule_dict = make_rulesdict(rules)
    combos = create_combinations(rule_dict)

    count = 0
    for mess in messages:
        if mess in combos: 
            count+=1
    return(count)

def check_message(mess, combos_42, combos_31):

    seg_length = len(combos_42[0])
    num_segs = int(len(mess)/seg_length)
    count_42 = 0
    count_31 = 0

    #check that first and second segment is in combos_42
    for i in range(2):
        segment = mess[i*seg_length:(i+1)*seg_length]
        if segment not in combos_42:
            return False
    count_42 = 2
    i=2
    #allow for more in 42, keep count
    while mess[i*seg_length:(i+1)*seg_length] in combos_42:
        count_42+=1
        i+=1
    
    #now check 31s
    while mess[i*seg_length:(i+1)*seg_length] in combos_31:
        count_31+=1
        i+=1

    if i < num_segs:
        return False

    if (count_31 > 0) and (count_31 < count_42):

        return True

    return False


def part2(filename):

    (rules, messages) = read_data(filename)
    
    rule_dict = make_rulesdict(rules)
    #all rules lead to 42 and 31
    combos_42 = create_combinations(rule_dict, first_rule = '42')
    combos_31 = create_combinations(rule_dict, first_rule = '31')

    matches = []

    for mess in messages:
        if check_message(mess, combos_42, combos_31):
            matches.append(mess)

    return(matches)
      

def run_tests():

    rules = [
        '0: 4 1 5',
        '1: 2 3 | 3 2',
        '2: 4 4 | 5 5',
        '3: 4 5 | 5 4',
        '4: "a"',
        '5: "b"',
    ]

    messages = [
        'ababbb',
        'bababa',
        'abbbab',
        'aaabbb',
        'aaaabbb',
    ]
    rule_dict = make_rulesdict(rules)
    combos = create_combinations(rule_dict)

    count = 0
    for mess in messages:
        if mess in combos: 
            count+=1
    assert(count==2)
    assert(part1("day19_test.txt") == 3)
    assert(len(part2("day19_test.txt")) == 12)



def day19():
    print("Part 1: ", part1("day19.txt"))
    print("Part 2: ", len(part2("day19.txt")))


if __name__ == "__main__":
    run_tests()
    day19()