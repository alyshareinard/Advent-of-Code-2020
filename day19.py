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
        if '|' in item and first == True:
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


def create_combinations_0(rules):
    from itertools import chain

    rule_dict={}
    first_rule = '0'
    for rule in rules:
        num, definition = rule.split(': ')
        if '"' in definition:
            rule_dict[num] = definition.replace('"', '')
        else:
            rule_dict[num] = definition.split(' ')
#    print('rules', rule_dict)

    rules = [rule_dict[first_rule]]
    print('starting with rule0', rules)
    possible = []

    count=0
    done = [] #will hold all combinations that have been played out
    while len(rules)>0:
        #deal with ors if we have them
        print("\nstarting while", len(rules))
        print(rules[0])
        print("num done", len(done))
        for rule in rules:

            if isdone(rule):
                done.append(''.join(rule))
                rules.remove(rule)
            else:
#                print("rule", rule)
                if '|' in chain(*rule):
                    (rule1, rule2) = reduce_ors(rule)
                    rules.append(rule1)
                    rules.append(rule2)
                    rules.remove(rule)
   
                else:
                    new_rule = []
                    for item in rule:
#                        print("item", item)
                        if item.isnumeric(): 
                            insert = rule_dict[item]
                            if '|' in insert or type(insert) == str:
                                new_rule.append(rule_dict[item])
                            else:
                                new_rule = new_rule + rule_dict[item]
       
                        else:
                            new_rule.append(item)
                    rules.remove(rule)
                    rules.append(new_rule)
#                if count<2:
#                    again=True
#                count+=1

#        print("rules")
#        for rule in rules:
#            print(rule)

    #now make the combos
    combos = []
    for rule in rules:
#        print(rule)
        combos.append(''.join(rule))
#    print('combos',done)
    return done


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


cap = 100

def create_combinations_0_queue(rules, longest = 100):

    from collections import deque

    rule_dict={}
    first_rule = '0'
    for rule in rules:
        num, definition = rule.split(': ')
        if '"' in definition:
            rule_dict[num] = definition.replace('"', '')
        else:
            rule_dict[num] = definition.split(' ')
#    print('rules', rule_dict)
    rules = deque()
    rules.append(rule_dict[first_rule])
    print('starting with rule0', rules)
    messcount = 0
    count=0
    done = [] #will hold all combinations that have been played out
    while len(rules)>0:
 
        count+=1
        if count % 1000000 == 0:

            print("\nin count", len(rules))


        rule = rules.pop()
        new_rules = process_rule(rule, rule_dict)
        for new_rule in new_rules:
            if isdone(new_rule):# and new_rule not in done:
                done.append(''.join(new_rule))
            elif len(new_rule)<longest:# and new_rule not in allrules:
                rules.insert(0, new_rule)

    #now make the combos
    combos = []
    for rule in rules:
#        print(rule)
        combos.append(''.join(rule))
#    print('combos',done)
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

    combos = create_combinations_0_queue(rules)

    count = 0
    for mess in messages:
        if mess in combos: 
            count+=1
    assert(count == 2)

def part1():
    (rules, messages) = read_data()
    longest = len(max(messages, key=len))

    combos = create_combinations_0_queue(rules, longest)

    count = 0
    for mess in messages:
        if mess in combos: 
            count+=1
    print("Part 1: ", count)

def part2():
    (rules, messages) = read_data_part2()

    #find longest message
    longest = len(max(messages, key=len))
    combos = create_combinations_0_queue(rules, longest)

    count = 0
    for mess in messages:
        if mess in combos: 
            count+=1
    print("Part 2: ", count)

def day19():
    part1()
    #part2()






if __name__ == "__main__":
    run_tests()
    day19()