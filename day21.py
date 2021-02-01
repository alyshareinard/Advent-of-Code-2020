import numpy as np
import math
from pandas.core.common import flatten

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
        foodlist_dict[count] = ingreds.split(' ')
        allergen_dict[count] = allergs.split(', ')
        count+=1
    return (foodlist_dict, allergen_dict)

def collect_possibilities(keys, foodlist_dict):
    #start with all the foods in the first item, then remove those that don't appear in subsequent items
    possibilities = foodlist_dict[keys[0]]

    if len(keys) == 1:
        return possibilities

    #there are multiple items - we processed the first already, so let's go through the rest
    keys = keys[1:]
    for key in keys:
        l_poss = []
        for food in possibilities:
            if food in foodlist_dict[key]:
                l_poss.append(food)
        possibilities = l_poss
    return possibilities

                
def narrow_to_final(all_food_match):

    all_food_match_final = {}
    while len(all_food_match)>0:
        notdone=False
        keys = list(all_food_match.keys())
        for key in keys:
            foods = all_food_match[key]
            if type(foods) !=list:
                all_food_match_final[key] = foods
                del all_food_match[key]
            elif len(foods)==1:
                all_food_match_final[key] = foods[0]
                del all_food_match[key]
            elif len(foods)>1:
                done = [all_food_match_final[x] for x in all_food_match_final]
                new_food=[]
                for food in foods:
                    if food not in done:
                        new_food.append(food)
                all_food_match[key] = new_food
                    
            else:
                print("something wrong here.  Allergens = ", allergens)
    return all_food_match_final
                
                    

def match_allergens(foodlist_dict, allergen_dict):

    allergens = set(flatten(allergen_dict.values()))
    
    all_food_match = {}

    #step through each allergen and collect all the keys that contain that allergen
    for allergen in allergens:
        mykeys = []
        for key in allergen_dict:
            if allergen in allergen_dict[key]:
                mykeys.append(key)
        #Then go collect all the possible ingredients that match that allergen
        all_food_match[allergen] = collect_possibilities(mykeys, foodlist_dict)

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

    all_foods =  list(flatten(foodlist_dict.values()))

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