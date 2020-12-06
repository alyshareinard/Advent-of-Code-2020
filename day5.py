def read_data():
    with open("day5.txt") as f:
        seat_db = f.read().split('\n')
    return seat_db

def parse_seat(seat):
    if seat == "":
        return (0, 0, 0)
    seat = seat.replace('B', '1').replace('F', '0').replace('R', '1').replace('L', '0')
    row = int(seat[0:7], 2)
    col = int(seat[7:], 2)
    seat_ID = row * 8 + col
    return(row, col, seat_ID)

def run_tests():
    seats = [
        'BFFFBBFRRR',
        'FFFBBBFRRR',
        'BBFFBBFRLL',
    ]
    for seat in seats: 
        (row, col, seat_ID) = parse_seat(seat)
        print(seat, row, col, seat_ID)
def day5():
    seats = read_data()
    highest_ID = 0
    seat_IDs = []
    for seat in seats:
        (row, col, seat_ID) = parse_seat(seat)
        seat_IDs.append(seat_ID)
        if seat_ID > highest_ID:
            highest_ID = seat_ID
    print("Part 1:", highest_ID)
    seat_IDs.sort()
    print(seat_IDs)
    next_seat = 0
    for val in seat_IDs:
        if val == next_seat:
            next_seat+=1
            
        elif val > next_seat:
            print("missing ", next_seat)
            next_seat = val+1
            
        

    
if __name__ == "__main__":
    run_tests()
    day5()