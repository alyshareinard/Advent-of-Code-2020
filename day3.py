def read_data():
    with open("day3.txt") as f:
        data= f.read().split('\n')
        data = data[:-1] #remove the last \n
        print("Length of map", len(data))
        print("Width of map", len(data[0]))
    return data

def walk_slope(trees, right = 3, down = 1):
    path = []
    right_loc = right
    down_loc = down
    width = len(trees[0])
    while down_loc < len(trees):
       
        if trees[down_loc][right_loc] == "#":
            path.append('X')
        else:
            path.append('O')
        down_loc+=down
        right_loc+=right
        if right_loc>=width:
            right_loc-=width
    return path 

def day3():
    trees = read_data()
    path = walk_slope(trees)
    print("Part 1 -- Number of trees is:", path.count('X'))

    path_counts = []
    path = walk_slope(trees, 1, 1)
    path_counts.append(path.count('X'))

    path = walk_slope(trees, 3, 1)
    path_counts.append(path.count('X'))

    path = walk_slope(trees, 5, 1)
    path_counts.append(path.count('X'))

    path = walk_slope(trees, 7, 1)
    path_counts.append(path.count('X'))

    path = walk_slope(trees, 1, 2)
    path_counts.append(path.count('X'))

    print("Part 2 -- Here is the product: ", product(path_counts))
    
def product(mylist):
    ans = 1
    for val in mylist:
        ans *= val
    return ans

def run_tests():
    path_counts = []
    trees = ['..##.......',
            '#...#...#..',
            '.#....#..#.',
            '..#.#...#.#',
            '.#...##..#.',
            '..#.##.....',
            '.#.#.#....#',
            '.#........#',
            '#.##...#...',
            '#...##....#',
            '.#..#...#.#']
            
    
    path = walk_slope(trees, 1, 1)
    assert(path.count('X') == 2)
    path_counts.append(path.count('X'))
    path = walk_slope(trees, 3, 1)
    assert(path.count('X') == 7)
    path_counts.append(path.count('X'))
    path = walk_slope(trees, 5, 1)
    assert(path.count('X') == 3)
    path_counts.append(path.count('X'))
    path = walk_slope(trees, 7, 1)
    assert(path.count('X') == 4)
    path_counts.append(path.count('X'))
    path = walk_slope(trees, 1, 2)
    assert(path.count('X') == 2)
    path_counts.append(path.count('X'))

    assert(product(path_counts)==336)


if __name__ == "__main__":
    run_tests()
    day3()