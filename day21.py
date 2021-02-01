import numpy as np
import math

def read_data():
    with open("day21.txt") as f:
        foodlist = f.read().split('\n')
    print(foodlist)
    foodlist = foodlist[:-1]
    return(foodlist)


def parse_allergens(foodlist):
    foodlist_dict={}
    allergen_dict={}
    count = 0
    for food in foodlist:
        (ingreds, allergs) = food.replace(')', '').split(' (contains ')
        ingreds = ingreds.split(' ')
        allergs = allergs.split(', ')
        foodlist_dict[count]=ingreds
        allergen_dict[count]=allergs
        count+=1
    return (foodlist_dict, allergen_dict)

def collect_possibilities(keys, foodlist_dict):
    possibilities = foodlist_dict[keys[0]]
    print("possibilities", possibilities)
    print('keys1 ', keys)
    if len(keys) > 0:
        keys = keys[1:]
        print('keys2 ', keys)
        for key in keys:
            l_poss = []
            for food in possibilities:
                print("checking ", food)
                if food in foodlist_dict[key]:
                    l_poss.append(food)
            possibilities = l_poss
    print(possibilities)
    return possibilities

                
def narrow_to_final(all_food_match):
    notdone = True
    all_food_match_final = {}
    while notdone:
        notdone=False
        keys = list(all_food_match.keys())
        for key in keys:
            allergens = all_food_match[key]
            if type(allergens) !=list:
                all_food_match_final[key] = allergens
                del all_food_match[key]
            elif len(allergens)==1:
                all_food_match_final[key] = allergens[0]
                del all_food_match[key]
            elif len(allergens)>1:
                notdone = True
                done = [all_food_match_final[x] for x in all_food_match_final]
                new_aller=[]
                for allergen in allergens:
                    if allergen not in done:
                        new_aller.append(allergen)
                all_food_match[key] = new_aller
                    
            else:
                print("something wrong here.  Allergens = ", allergens)
    print("done? ", all_food_match_final)
    return all_food_match_final
                
                    

def match_allergens(foodlist_dict, allergen_dict):
    print("foods\n", foodlist_dict)
    print("allergens\n", allergen_dict)
    allergens = []
    for key in allergen_dict:
        for item in allergen_dict[key]:
            allergens.append(item)

    allergens = set(allergens)
    print(allergens)
    all_food_match = {}

    for allergen in allergens:
        print("allergen:", allergen)
        mykeys = []
        for key in allergen_dict:
            if allergen in allergen_dict[key]:
                mykeys.append(key)
        all_food_match[allergen] = collect_possibilities(mykeys, foodlist_dict)

    print(all_food_match)
    all_food_final = narrow_to_final(all_food_match)

    return all_food_final

def part1(foodlist):

    (foodlist_dict, allergen_dict) = parse_allergens(foodlist)

    allerg_food = match_allergens(foodlist_dict, allergen_dict)

    ###PART 2 ###
    zipped_foods = sorted(zip(allerg_food.keys(), allerg_food.values()))
    sorted_foods = [x for _, x in zipped_foods]
    print("Part 2: ", ','.join(sorted_foods))
    #####

    all_foods = []
    for key in foodlist_dict:
        for item in foodlist_dict[key]:
            all_foods.append(item)

    all_foods_once = list(set(all_foods))

    for key in allerg_food:
        all_foods_once.remove(allerg_food[key])
    count=0
    for food in all_foods_once:
        count+=all_foods.count(food)
    return count

def run_tests():
    foodlist = [
        'mxmxvkd kfcds sqjhc nhms (contains dairy, fish)',
        'trh fvjkl sbzzf mxmxvkd (contains dairy)',
        'sqjhc fvjkl (contains soy)',
        'sqjhc mxmxvkd sbzzf (contains fish)',

    ]
    assert(part1(foodlist))==5

def day21():
    foodlist = read_data()
    print("Part 1:", part1(foodlist))




if __name__ == "__main__":
    #run_tests()
    day21()