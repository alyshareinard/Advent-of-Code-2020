import numpy as np
import math

def read_data():
    with open("day19.txt") as f:
        rules_messages = f.read().split('\n\n')
    rules = rules_messages[0].split("\n")
    messages = rules_messages[1].split("\n")
    messages = messages[:-1]
    return (rules, messages)


def read_data_part2():
    with open("day19_part2.txt") as f:
        rules_messages = f.read().split('\n\n')
    rules = rules_messages[0].split("\n")
    messages = rules_messages[1].split("\n")
    messages = messages[:-1]
    return (rules, messages)

def reduce_ors(rule):
    rule1 = []
    rule2 = []
    #just do first or
#    print("rule in or", rule)
    first = True
    for item in rule:
#        print("item in or", item)
        if '|' in item  and item != '|' and first == True:
            split = item.index('|')
#            print("split", split)
#            print(item[:split])
#            print(item[split+1:])
            rule1 = rule1 + item[:split]
            rule2 = rule2 + item[split+1:]
            first = False
        else:
            rule1.append(item)
            rule2.append(item)
#    print("rule1", rule1)
#    print("rule2", rule2)
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
#    if '|' in rule:
        (rule1, rule2) = reduce_ors(rule)
        return([rule1, rule2])
    else:
        new_rule = []
        for item in rule:
#            print("ITEMS", item)
            if item.isnumeric(): 
                insert = rule_dict[item]
#                print("insert", insert)
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

def create_combinations(rule_dict, first_rule = '0', longest = 100):

    from collections import deque


#    print('rules', rule_dict)
    print("first_rule", first_rule)
    rules = deque()
    if '|' in rule_dict[first_rule]:
        print("first one has an or")
        rules.append([rule_dict[first_rule]])
    else:
        print("no or to see here")
        rules.append(rule_dict[first_rule])

    print('starting with rule0', rules)
    messcount = 0
    count=0
    done = [] #will hold all combinations that have been played out
    while len(rules)>0:
 
        count+=1
        if count % 1000000 == 0:

            print("\nin count", len(rules), len(done))


        rule = rules.pop()

        new_rules = process_rule(rule, rule_dict)
        for new_rule in new_rules:
            if isdone(new_rule):# and new_rule not in done:
                done.append(''.join(new_rule))
            elif len(new_rule)<longest:# and new_rule not in allrules:
                rules.insert(0, new_rule)

    return done


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
    assert(count == 2)

def part1():
    (rules, messages) = read_data()

    rule_dict = make_rulesdict(rules)
    combos = create_combinations(rule_dict)

    count = 0
    for mess in messages:
        if mess in combos: 
            count+=1
    print("Part 1: ", count)

def part2():
#    (rules, messages) = read_data_part2()
    (rules, messages) = read_data()
    
    rule_dict = make_rulesdict(rules)

    combos_42 = create_combinations(rule_dict, first_rule = '42')
    combos_31 = create_combinations(rule_dict, first_rule = '31')

    #create markers for rule 8 and 11


#    temp = rule_dict['8']
#    print("TESTING TMP", temp+['e'])
#    rule_dict['8'] = rule_dict['8'] + ['e']

#    print("TESTING", rule_dict['8'])
#    rule_dict['11'] =  rule_dict['11'] + ['f']
    
#    combos = create_combinations(rule_dict)

    #find longest message
    longest = len(max(messages, key=len))
    print("now doing combos")
    count = 0

    combos = ['ef']
    done = []


    for rule42 in combos_42:
        for rule31 in combos_31:
            for i in range(1, 10):
                for j in range(1, 10):
#                    print(i, j, rule42, rule31)
#                    print(i*rule42 + j*rule42 + j*rule31)
                    done.append(i*rule42 + j*rule42 + j*rule31)
#            print(len(done[-1]))


    print(len(done))
    for i in range(100):
        print(done[i])
    print("now checking combos")



#    combos = create_combinations(rules, longest)
    messages.append('abbbabbaabbbabbababaaaab')
    count = 0
    for mess in messages:
        print('mess', mess)
        print('done', done[0])
        if mess in done: 

            count+=1
            print("found one")
    print("Part 2: ", count)

def day19():
#    part1()
    part2()








if __name__ == "__main__":
#    run_tests()
    day19()