import re
with open('practice_d2p1.txt', 'r') as f:
    puzzles = f.read()
def part1(puzzles):

    conditions = {'red': 12, 'green': 13, 'blue': 14}
    sum_of_game_ids = 0
    sectioned_list = puzzles.split("\n")
    
    #grouped = sectioned_list.split(";")
    #print(grouped)
    possibleid = False
    for id, game in enumerate(sectioned_list, start=1):
        game_split = game.split(': ')
        for str_of_group in game_split[1:]:
            pairs = str_of_group.split('; ')
            for pair in pairs:
    
                finalpair = pair.split(', ')
                print(finalpair)
                for kv in finalpair:
                    number, colour = kv.split()
                    if int(number) >= conditions[colour]:
                        print(number)
                        print(conditions[colour])
                        possibleid == True
                    
        if possibleid == True:
            sum_of_game_ids+=id

                        
    return sum_of_game_ids
        
    
print(part1(puzzles))
    
