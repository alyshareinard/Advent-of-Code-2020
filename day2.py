def read_data():
    with open("day2.txt") as f:
        pass_db = f.read().split('\n')
    return pass_db

def check_password(pwdline):
    if pwdline == '':
        return False
    (temp, letter, pwd) = pwdline.split()
    (min_times, max_times) = temp.split('-')
    min_times = int(min_times)
    max_times = int(max_times)
    
    letter = letter[:-1] #remove the ':'

    count = pwd.count(letter)
    if count >= min_times and count<=max_times:
        return True
    else:
        return False

def check_password2(pwdline):
    if pwdline == '':
        return False  #remove any blank lines
    (temp, letter, pwd) = pwdline.split()
    (ind1, ind2) = temp.split('-')
    ind1 = int(ind1) - 1
    ind2 = int(ind2) - 1
    
    letter = letter[:-1] #remove the ':'
    if bool(pwd[ind1] == letter) ^ bool(pwd[ind2] == letter):
        return True
    else:
        return False

def run_tests():
    num_good = 0
    num_good2 = 0
    pass_db = ['1-3 a: abcde',
        '1-3 b: cdefg',
        '2-9 c: ccccccccc']   
    for password in pass_db:
        num_good += check_password(password)
        num_good2 += check_password2(password)
    assert(num_good == 2) 
    assert(num_good2 == 1)  



def find_soln(pass_db):
    num_good = 0
    num_good2 = 0
    for password in pass_db:
        num_good += check_password(password)
        num_good2 += check_password2(password)
    print("Part 1: The number of good passwords is: ", num_good)
    print("Part 2: The number of good passwords is: ", num_good2)

def day2():
    pass_db = read_data()
    find_soln(pass_db)

    

if __name__ == "__main__":
    run_tests()
    day2()