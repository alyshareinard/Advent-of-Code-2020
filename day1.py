

def read_data():
    with open("day1.txt") as f:
        expenses = f.read().split()
    expenses = [int(x) for x in expenses]
    return expenses

def find_soln1(expenses):
    from itertools import permutations
    perms = permutations(expenses, 2)
    for perm in perms:
        (x, y) = perm
        if x + y == 2020:
            print ("answer to part 1 is: ", x * y)
            return 

def find_soln2(expenses):
    from itertools import permutations
    perms = permutations(expenses, 3)
    for perm in perms:
        (x, y, z) = perm
        if x + y + z == 2020:
            print ("answer to part 2 is: ", x * y * z)
            return 

def run_tests():
    expenses = [1721, 979, 366, 299, 675, 1456]    
    find_soln1(expenses)

def day1():
    expenses = read_data()
    find_soln1(expenses)
    find_soln2(expenses)
    

if __name__ == "__main__":
    run_tests()
    day1()
