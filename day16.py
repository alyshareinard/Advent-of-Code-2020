import numpy as np

def read_data():
    with open("day16.txt") as f:
        inputs = f.read().split('\n\n')
    notes = []
    for item in inputs:
        notes.append(item.split('\n'))
    #take care of last newline
    notes[2] = notes[2][:-1]
    return notes

def part1(requirements, nearby_tickets):
    #flatten my requirements and ticket values
    all_requirements = list(set([x for sublist in requirements.values() for x in sublist]))
    all_ticketvals = list([x for sublist in nearby_tickets for x in sublist])
    invalid = []
    #loop through ticketsvals and pull out invalid ones
    for val in all_ticketvals:
        if val not in all_requirements:
            invalid.append(val)
    return(sum(invalid))


def validate_ticket(requirements, ticket):
    all_requirements = list(set([x for sublist in requirements.values() for x in sublist]))
    for val in ticket:
        if val not in all_requirements:
            return False
    return True

def validate_field(requirements, ticket_field):
    possible_matches = []


    for key, vals in requirements.items():
        addit=True
        for item in ticket_field:
            if item not in vals:
                addit=False
        if addit: 
            possible_matches.append(key)
        

    return(possible_matches)

def determine_fields(field_dict):
    solution = {}
    done = []
    while len(field_dict) >0:
        for columns, fields in field_dict.items():
            for field in fields:
                if field in solution.keys():
                    fields.remove(field)

            if len(fields) == 1:
                solution[fields[0]] = columns
                done.append(columns)
                field_dict.pop(columns)
                break
    return(solution)

def collect_ticketcols(requirements, other_tickets, my_ticket):
    ticket_fields = np.array([my_ticket])
    for ticket in other_tickets:
        if validate_ticket(requirements, ticket):
            ticket_fields = np.append(ticket_fields, [ticket], axis=0)
    #transpose the array to make it easier to think about (different fields are now in columns instead of rows)
    ticket_fields = ticket_fields.transpose()
    return(ticket_fields)


def find_all_possibles(requirements, ticket_fields):
    field_dict = {}
    for i in range(len(ticket_fields)):
        possible_matches = validate_field(requirements, ticket_fields[i, :])
        field_dict[i] = possible_matches
    return(field_dict)

def part2(requirements, other_tickets, my_ticket):


    ticket_fields = collect_ticketcols(requirements, other_tickets, my_ticket)

    #now step through the columns and find all fields that would be possible based on requirements
    field_dict = find_all_possibles(requirements, ticket_fields)
        
    #finally, determine the fields that match each column
    solution = determine_fields(field_dict)

    print("Part 2 solution", solution)

    return(solution)

def parse_notes(notes):
    requirements ={}
    for req in notes[0]:
        key, val = req.split(': ')
        val = val.split(' or ')
        values = []
        for seg in val:
            seg = seg.split('-')
            values+= [x for x in range(int(seg[0]), int(seg[1])+1)]
        requirements[key] = values
    my_ticket = [int(x) for x in notes[1][1].split(',')]
    nearby_tickets = []
    for ticket in notes[2][1:]:
        nearby_tickets.append([int(x) for x in ticket.split(',')])
    return(requirements, my_ticket, nearby_tickets)

def run_tests():
    notes = [
        ['class: 1-3 or 5-7',
        'row: 6-11 or 33-44',
        'seat: 13-40 or 45-50',],
        ['your ticket:',
        '7,1,14',],
        ['nearby tickets:',
        '7,3,47',
        '40,4,50',
        '55,2,20',
        '38,6,12'],
    ]

    (requirements, my_ticket, nearby_tickets) = parse_notes(notes)
    assert(part1(requirements, nearby_tickets)==71)

    notes = [
        ['class: 0-1 or 4-19',
        'row: 0-5 or 8-19',
        'seat: 0-13 or 16-19'],
        ['your ticket:',
        '11,12,13'],
        ['nearby tickets:',
        '3,9,18',
        '15,1,5',
        '5,14,9']
    ]
    (requirements, my_ticket, nearby_tickets) = parse_notes(notes)

    part2(requirements, nearby_tickets, my_ticket)
    

   
def day16():
    notes = read_data()
    (requirements, my_ticket, nearby_tickets) = parse_notes(notes)
    print("Part 1:", part1(requirements, nearby_tickets))

    part2sol = part2(requirements, nearby_tickets, my_ticket)

    sol = 1
    for key, val in part2sol.items():
        if key[0:9] ==  'departure':
            sol *= my_ticket[val]
    print("Part 2:", sol)
    
if __name__ == "__main__":
    run_tests()
    day16()