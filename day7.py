def read_data():
    with open("day7.txt") as f:
        rule_db = f.read().split('\n')
    return rule_db

def parse_rule(rule):
    rule = rule.split(' contain ')
    key = rule[0].replace(' ', '').replace('bags', '').replace('bag', '')
    contains = [x.replace('.', '').replace('bags', '').replace('bag', '') for x in rule[1].split(', ')]
    vals = []
    for contain in contains:
        if contain.strip() != "no other":
            contain = contain.split(' ')

            num = contain[0]
            bagdesc = ''.join(contain[1:])
            vals.append((bagdesc, num))
    return(key, vals)

def contains_shinygold(rules, target):
    tocheck = [target]

    while (tocheck != []):
        target = tocheck[0]
        for val in rules[target]:
            (bag, num) = val
            tocheck.append(bag) #add interior bags to our "to check" list
            if bag == 'shinygold':
                return True
        tocheck.remove(target)
    return False

def inside_shinygold(rules):
    tocheck = ['shinygold']
    bag_count=0
    while (tocheck != []):
        target = tocheck[0]
        for val in rules[target]:
            (bag, num) = val
            for _ in range(int(num)):
                tocheck.append(bag)  # add any interior bags to the list to check
            bag_count+=int(num)
        tocheck = tocheck[1:]
    return bag_count



def run_tests():
    rules = [
        'light red bags contain 1 bright white bag, 2 muted yellow bags.',
        'dark orange bags contain 3 bright white bags, 4 muted yellow bags.',
        'bright white bags contain 1 shiny gold bag.',
        'muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.',
        'shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.',
        'dark olive bags contain 3 faded blue bags, 4 dotted black bags.',
        'vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.',
        'faded blue bags contain no other bags.',
        'dotted black bags contain no other bags.',
    ]
    rules_dict = {}
    for rule in rules:
        (key, vals) = parse_rule(rule)
        rules_dict[key]=vals

    count = 0
    for key in rules_dict:
        count+=contains_shinygold(rules_dict, key)
    assert(count == 4)


    count = inside_shinygold(rules_dict)
    assert(count == 32)


def day5():
    rules = read_data()
    rules_dict = {}
    for rule in rules:
        (key, vals) = parse_rule(rule)
        rules_dict[key]=vals

    count = 0
    for key in rules_dict:
        count+=contains_shinygold(rules_dict, key)
    print("Part 1: ", count)
    
    count = inside_shinygold(rules_dict)
    print("Part 2: ", count)

    
if __name__ == "__main__":
    run_tests()
    day5()