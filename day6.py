def read_data():
    with open("day6.txt") as f:
        forms_db = f.read().split('\n\n')
    return forms_db

def check_form(form):
    items=[]
    for item in form:
        if item.isalpha():
            items.append(item)

    return len(set(items))

def check_form2(form):
    items=[]
    for item in form:
        if item.isalpha():
            items.append(item)
    items = set(items)

    form = form.split("\n")

    for person in form:
        temp_items = [x for x in items]
        for item in temp_items:
            if item not in person:
                items.remove(item)
    return len(items)

def run_tests():
    with open("day6_test.txt") as f:
        forms_db = f.read().split('\n\n')
    yeses = 0
    for form in forms_db:
        yeses = yeses + check_form(form)
    assert(yeses == 11)
    yeses = 0
    for form in forms_db:
        yeses = yeses + check_form2(form)
    assert(yeses == 6)
        

def day5():
    forms = read_data()
    yeses = 0
    for form in forms:
        yeses = yeses + check_form(form)  
    print("Part 1: ", yeses)         
    yeses = 0
    for form in forms:
        yeses = yeses + check_form2(form)  
    print("Part 2: ", yeses) 

    
if __name__ == "__main__":
    run_tests()
    day5()