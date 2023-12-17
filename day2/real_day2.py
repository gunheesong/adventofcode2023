import re
with open('real_day2.txt', 'r') as f:
    puzzles = f.read()
def part1(puzzles):

    conditions = {'red': 12, 'green': 13, 'blue': 14}
    sum_of_game_ids = 0
    sectioned_list = puzzles.split("\n")
    
    #grouped = sectioned_list.split(";")
    #print(grouped)
    
    for id, game in enumerate(sectioned_list, start=1):
        possibleid = True
        game_split = game.split(': ')
        for str_of_group in game_split[1:]:
            pairs = str_of_group.split('; ')
            for pair in pairs:
                finalpair = pair.split(', ')
                for kv in finalpair:               
                    number, colour = kv.split()
                    if int(number) > conditions[colour]:
                        possibleid = False
            if possibleid is True:
                sum_of_game_ids+=id
        

                     
    return sum_of_game_ids

def part2(puzzles):
         
    sectioned_list = puzzles.split("\n")
    sum_of_sets = 0
    for id, game in enumerate(sectioned_list, start=1):
        conditions = {'red': 0, 'green': 0, 'blue': 0}
        power_of_sets = 1
        game_split = game.split(': ')
        for str_of_group in game_split[1:]:
            pairs = str_of_group.split('; ')
            for pair in pairs:
                finalpair = pair.split(', ')
                for kv in finalpair:
                    number, colour = kv.split()
                    #print(number)
                    if conditions[colour] < int(number):
                        conditions[colour] = int(number)
            #print(id, conditions)
                    #print(conditions)
            
        for value in conditions.values():
                
            power_of_sets *= value
                #print(power_of_sets)
        sum_of_sets += power_of_sets
        
        
    return sum_of_sets
print(part2(puzzles))
