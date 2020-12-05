def read_data():
    with open("day4.txt") as f:
        pass_db = f.read().split('\n\n')
    return pass_db

def run_tests():
    batch = [
        'ecl:gry pid:860033327 eyr:2020 hcl:#fffffd byr:1937 iyr:2017 cid:147 hgt:183cm',
        'iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884 hcl:#cfa07d byr:1929',
        'hcl:#ae17e1 iyr:2013 eyr:2024 ecl:brn pid:760753108 byr:1931 hgt:179cm',
        'hcl:#cfa07d eyr:2025 pid:166559648 iyr:2011 ecl:brn hgt:59in',
    ]
    check = 0
    for passport in batch:
        pass_dict = parse_passport(passport)
        check += check_passport2(parse_passport(passport))
    assert(check == 2)
        

def parse_passport(passport):
    pass_dict = {}
    passport = passport.replace('\n', ' ')
    fields = passport.split(" ")
    for field in fields:
        if ':' in field:
            (mykey, myvalue) = field.split(':')
            pass_dict[mykey] = myvalue
    return pass_dict

def check_passport(passport):
    if ('byr' in passport and 'iyr' in passport and 
        'eyr' in passport and 'hgt' in passport and
        'hcl' in passport and 'ecl' in passport and 
        'pid' in passport):  
        return True
    return False


def check_passport2(passport):
    import re

    if (not('byr' in passport) or 
        not('iyr' in passport) or
        not('eyr' in passport) or
        not('hgt' in passport) or
        not('hcl' in passport) or 
        not('ecl' in passport) or 
        not('pid' in passport)): 
        return False

    if len(passport['byr']) != 4 or int(passport['byr']) < 1920 or int(passport['byr']) > 2002:
        return False
    if len(passport['iyr']) != 4 or int(passport['iyr']) < 2010 or int(passport['iyr']) > 2020:
        return False
    if len(passport['eyr']) != 4 or int(passport['eyr']) < 2020 or int(passport['eyr']) > 2030:
        return False
    if passport['hgt'][-2:] == 'cm':
        if (int(passport['hgt'][:-2])<150 or int(passport['hgt'][:-2])>193):
            return False
    elif passport['hgt'][-2:] == 'in':
        if (int(passport['hgt'][:-2])<59 or int(passport['hgt'][:-2])>76):
            return False
    else:
        return False
    if not (re.search('^#(?:[0-9a-f]{6})$', passport['hcl'])):
        return False
    if passport['ecl'] not in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
        return False
    if len(passport['pid']) != 9: 
        return False
    
    return True #if we made it through the gauntlet, we're gold
     
def day4():
    batch = read_data()
    check = 0
    check2 = 0
    for passport in batch:
        pass_dict = parse_passport(passport)
        check += check_passport(parse_passport(passport))
        check2 += check_passport2(parse_passport(passport))
    print("Part 1: ", check)
    print("Part 2: ", check2)
    
if __name__ == "__main__":
    run_tests()
    day4()