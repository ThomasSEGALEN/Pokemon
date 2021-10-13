import random
from os import system, name

#   Init variables
#   Pokedollars
balance = 10000

#   Pokemons list - id, "name", minSpawn, maxSpawn, nbCatch, attack, defense, resistance
pokemons = [
    [1, "Bulbasaur", 0, 60, 0, 49, 49, 20], [2, "Charmander", 61, 121, 0, 52, 43, 20], [3, "Squirtle", 122, 182, 0, 48, 65, 20], [4, "Caterpie", 183, 263, 0, 30, 35, 0], 
    [5, "Weedle", 264, 344, 0, 35, 30, 0], [6, "Pidgey", 345, 425, 0, 45, 40, 0], [7, "Rattata", 426, 506, 0, 56, 35, 0], [8, "Spearow", 507, 587, 0, 60, 30, 0], 
    [9, "Ekans", 588, 658, 0, 60, 44, 0], [10, "Pikachu", 659, 719, 0, 55, 40, 20], [11, "Sandshrew", 720, 770, 0, 75, 85, 25], [12, "Nidoran ♀️", 771, 821, 0, 47, 52, 20], 
    [13, "Nidoran ♂️", 822, 872, 0, 57, 40, 20], [14, "Clefairy", 873, 923, 0, 45, 48, 20], [15, "Vulpix", 924, 974, 0, 41, 40, 25], [16, "Jigglypuff", 975, 1025, 0, 45, 20, 20], 
    [17, "Zubat", 1026, 1076, 0, 45, 35, 25], [18, "Golbat", 1077, 1127, 0, 80, 70, 25], [19, "Oddish", 1128, 1178, 0, 50, 55, 20], [20, "Paras", 1179, 1229, 0, 70, 55, 20], 
    [21, "Venonat", 1230, 1280, 0, 55, 50, 20], [22, "Diglett", 1281, 1351, 0, 55, 25, 10], [23, "Meowth", 1352, 1412, 0, 45, 35, 20], [24, "Psyduck", 1413, 1483, 0, 52, 48, 25], 
    [25, "Mankey", 1484, 1544, 0, 80, 35, 25], [26, "Growlithe", 1545, 1605, 0, 70, 45, 25], [27, "Poliwag", 1606, 1666, 0, 50, 40, 20], [28, "Abra", 1667, 1727, 0, 20, 15, 20], 
    [29, "Machop", 1728, 1788, 0, 80, 50, 25], [30, "Bellsprout", 1789, 1849, 0, 75, 35, 20], [31, "Tentacool", 1850, 1910, 0, 40, 35, 25], [32, "Geodude", 1911, 1971, 0, 80, 100, 25], 
    [33, "Ponyta", 1972, 2032, 0, 85, 55, 25], [34, "Slowpoke", 2033, 2093, 0, 65, 65, 20], [35, "Magnemite", 2094, 2154, 0, 35, 70, 25], [36, "Doduo", 2155, 2215, 0, 85, 45, 20], 
    [37, "Seel", 2216, 2276, 0, 45, 55, 10], [38, "Grimer", 2277, 2337, 0, 80, 50, 20], [39, "Shellder", 2338, 2398, 0, 65, 100, 20], [40, "Gastly", 2399, 2459, 0, 35, 30, 30], 
    [41, "Onix", 2460, 2500, 0, 45, 160, 30], [42, "Drowzee", 2501, 2561, 0, 48, 45, 25], [43, "Krabby", 2561, 2621, 0, 105, 90, 20], [44, "Voltorb", 2622, 2682, 0, 30, 50, 25], 
    [45, "Exeggcute", 2683, 2733, 0, 40, 80, 10], [46, "Cubone", 2734, 2784, 0, 50, 80, 25], [47, "Lickitung", 2785, 2845, 0, 55, 75, 30], [48, "Koffing", 2846, 2906, 0, 65, 95, 20], 
    [49, "Rhyhorn", 2907, 2967, 0, 85, 95, 25], [50, "Chansey", 2968, 3028, 0, 5, 5, 30], [51, "Tangela", 3029, 3089, 0, 55, 115, 20], [52, "Kangaskhan", 3090, 3140, 0, 95, 80, 35], 
    [53, "Horsea", 3141, 3201, 0, 40, 70, 25], [54, "Goldeen", 3202, 3252, 0, 67, 60, 20], [55, "Seaking", 3253, 3303, 0, 92, 65, 20], [56, "Staryu", 3304, 3354, 0, 45, 55, 25], 
    [57, "Mr. Mime", 3355, 3405, 0, 45, 65, 20], [58, "Scyther", 3406, 3446, 0, 110, 80, 35], [59, "Jynx", 3447, 3497, 0, 50, 35, 20], [60, "Electabuzz", 3498, 3558, 0, 83, 57, 30], 
    [61, "Magmar", 3559, 3619, 0, 95, 57, 30], [62, "Pinsir", 3620, 3680, 0, 125, 100, 30], [63, "Tauros", 3681, 3721, 0, 100, 95, 35], [64, "Magikarp", 3722, 3752, 0, 10, 55, 30], 
    [65, "Gyarados", 3753, 3773, 0, 125, 79, 45], [66, "Lapras", 3774, 3794, 0, 85, 80, 45], [67, "Ditto", 3795, 3845, 0, 48, 48, 40], [68, "Eevee", 3846, 3926, 0, 55, 50, 30], 
    [69, "Porygon", 3927, 3977, 0, 60, 70, 20], [70, "Omanyte", 3978, 4038, 0, 40, 100, 20], [71, "Kabuto", 4039, 4099, 0, 80, 90, 20], [72, "Aerodactyl", 4100, 4140, 0, 105, 65, 35], 
    [73, "Snorlax", 4141, 4181, 0, 110, 65, 35], [74, "Articuno", 4182, 4192, 0, 85, 100, 50], [75, "Zapdos", 4193, 4203, 0, 90, 85, 50], [76, "Moltres", 4204, 4214, 0, 100, 90, 50], 
    [77, "Dratini", 4215, 4245, 0, 64, 45, 35], [78, "Dragonair", 4246, 4276, 0, 84, 65, 40], [79, "Dragonite", 4277, 4297, 0, 134, 95, 45], [80, "Mewtwo", 4298, 4308, 0, 110, 90, 50], 
    [81, "Mew", 4309, 4319, 0, 100, 10, 500], [82, "Vaporeon", 4320, 4380, 0, 65, 60, 35], [83, "Jolteon", 4381, 4441, 0, 65, 60, 35], [84, "Pyroli", 4442, 4502, 0, 130, 60, 35], 
    [85, "Espeon", 4503, 4563, 0, 65, 60, 35], [86, "Umbreon", 4564, 4624, 0, 65, 110, 35], [87, "Togepi", 4625, 4695, 0, 20, 65, 30], [88, "Scizor", 4696, 4736, 0, 130, 100, 35], 
    [89, "Porygon2", 4737, 4787, 0, 80, 90, 25], [90, "Raikou", 4788, 4808, 0, 85, 75, 50], [91, "Entei", 4809, 4829, 0, 115, 85, 50], [92, "Suicune", 4830, 4850, 0, 75, 115, 50], 
    [93, "Larvitar", 4851, 4881, 0, 64, 50, 35], [94, "Pupitar", 4882, 4912, 0, 84, 70, 40], [95, "Tyranitar", 4913, 4933, 0, 134, 110, 45], [96, "Lugia", 4934, 4944, 0, 90, 130, 50], 
    [97, "Ho-Oh", 4945, 4955, 0, 130, 90, 50], [98, "Celebi", 4956, 4976, 0, 100, 100, 50], [99, "Latios", 4977, 5007, 0, 90, 80, 45], [100, "Latias", 5008, 5038, 0, 80, 90, 45]
]

#   Pokeballs list - "name", minCatch, maxCatch, price
pokeballs = [
    ["Pokeball", 30, 200], ["Superball", 50, 600], ["Hyperball", 70, 1200], ["Masterball", 100, 50000]
]

#   Pokeballs inventory - "name", amount
inventory_pokeballs = [
    ["Pokeball", 30], ["Superball", 0],["Hyperball", 500], ["Masterball", 100]
]

#   Pokemons inventory
inventory_pokemons = [
    [0, "Victini", 0, 0, 1, 100, 100, 0]
]


#   Clear function - clear screen

def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')


#   Spawn function - spawn a pokemon with which the player can interact

def spawn():
    global pokemon_spawn
    global pokemon_spawn_stats
    global pokemon_spawn_index
    total_range = 0

    for i in range (0, len(pokemons)):
        total_range += pokemons[i][3] - pokemons[i][2]
    # print(total_range)
    random_pokemon = (random.randint(0, total_range))
    # print(random_pokemon)
    for i in range (0, len(pokemons)-1):
        if random_pokemon >= pokemons[i][2] and random_pokemon <= pokemons[i][3]:
            pokemon_spawn = pokemons[i][1]
            pokemon_spawn_stats = pokemons[i]
            pokemon_spawn_index = i
            print("Wild", end=" ")
            print(pokemon_spawn, end=" ")
            print("spawned !\n")
    print("Choose your action:", end="")
    print("\n1: Fight | 2: Catch | Enter: Flee")
    input_spawn = input()
    if input_spawn == "1":
        clear()
        fight()
    elif input_spawn == "2":
        clear()
        catch()
    elif input_spawn == "":
        clear()
        play()
    else:
        clear()
        spawn()


#   Fight function - allow player to fight Pokemons and win Pokedollars

def fight():
    global balance

    print("Wild", end=" ")
    print(pokemon_spawn, end=" ")
    print("spawned !\n")
    print("Enter: Flee", end="")
    print("\nSelect your Pokemon:\n")
    for i in range (0, len(inventory_pokemons)):
        print("Pokemon", i+1, ":", inventory_pokemons[i][1])
    input_fight = input()
    if input_fight == "":
        clear()
        play()
    elif input_fight == "0" or int(input_fight) > len(inventory_pokemons):
        clear()
        fight()
    elif int(input_fight) <= len(inventory_pokemons):
        clear()
        print("Wild", end=" ")
        print(pokemon_spawn, end=" ")
        print("spawned !")
        pokemon_stats = inventory_pokemons[int(input_fight)-1]
        pokemon_fight = inventory_pokemons[int(input_fight)-1][1]
        # print(pokemon_stats)
        # print(pokemon_spawn_stats)
        pokemon_ratio_1 = int((pokemon_stats[4] / pokemon_stats[5])*100)
        pokemon_ratio_2 = int((pokemon_spawn_stats[4] / pokemon_spawn_stats[5])*100)
        # print(pokemon_ratio_1)
        # print(pokemon_ratio_2)
        ratio_range = pokemon_ratio_1 + pokemon_ratio_2
        # print(ratio_range)
        ratio_random = random.randint(0, ratio_range)
        # print(ratio_random)
        print("\n", end="")
        print(pokemon_fight, "VS", pokemon_spawn)
        if ratio_random < pokemon_ratio_1:
            print("Your Pokemon >", end=" ")
            print(pokemon_fight, "attacks")
            print("Enemy >", end=" ")
            print(pokemon_spawn, "fainted")
            pokedollars = random.randint(1, 2000)
            balance += pokedollars
            print("+", end="")
            print(pokedollars, "Pokedollars")
            print("Balance:", balance, "Pokedollars")
        else:
            print("Enemy >", end=" ")
            print(pokemon_spawn, "attacks")
            print("Your Pokemon >", end=" ")
            print(pokemon_fight, "fainted")
    else:
        clear()
        fight()
    print("\nEnter: Continue")
    input_continue = input()
    if input_continue == "" or input_continue:
        play()


#   Catch function - allow player to catch Pokemons

def catch():
    select_pokeball = False
    pokemon_different = False

    print("Wild", end=" ")
    print(pokemon_spawn, end=" ")
    print("spawned !")
    while select_pokeball == False:
        print("\nChoose your pokeball:\n", end="")
        print("1: Pokeball", inventory_pokeballs[0][1], end="")
        print("x | 2: Superball", inventory_pokeballs[1][1], end="")
        print("x | 3: Hyperball", inventory_pokeballs[2][1], end="")
        print("x | 4: Masterball", inventory_pokeballs[3][1], end="x | Enter: Flee\n")
        input_ball = input()
        resistance = pokemon_spawn_stats[6]
        # print(resistance)
        if input_ball == "":
            clear()
            play()
        else:
            catch_chance = pokeballs[int(input_ball)-1][1] - ((pokeballs[int(input_ball)-1][1] * resistance)/100)
        # print(catch_chance)
        if input_ball == "1":
            clear()
            print("Wild", end=" ")
            print(pokemon_spawn, end=" ")
            print("spawned !")
            if inventory_pokeballs[0][1] > 0:
                inventory_pokeballs[0][1] -= 1
                print("\nPokeball thrown")
                select_pokeball = True
                if random.randint(0, 100) <= catch_chance:
                    pokemons[pokemon_spawn_index][4] += 1
                    for i in range (0, len(inventory_pokemons)):
                        if inventory_pokemons[i][1] != pokemon_spawn:
                            pokemon_different = True
                        else:
                            pokemon_different = False
                            break
                    if pokemon_different == True:
                        inventory_pokemons.append(pokemon_spawn_stats)
                    print(pokemon_spawn, "catched")
                else:
                    print(pokemon_spawn, "escaped")
            else:
                print("\nNo Pokeball in your bag")
        elif input_ball == "2":
            clear()
            print("Wild", end=" ")
            print(pokemon_spawn, end=" ")
            print("spawned !")
            if inventory_pokeballs[1][1] > 0:
                inventory_pokeballs[1][1] -= 1
                print("\nSuperball thrown")
                select_pokeball = True
                if random.randint(0, 100) <= catch_chance:
                    pokemons[pokemon_spawn_index][4] += 1
                    for i in range (0, len(inventory_pokemons)):
                        if inventory_pokemons[i][1] != pokemon_spawn:
                            pokemon_different = True
                        else:
                            pokemon_different = False
                            break
                    if pokemon_different == True:
                        inventory_pokemons.append(pokemon_spawn_stats)
                    print(pokemon_spawn, "catched")
                else:
                    print(pokemon_spawn, "escaped")
            else:
                print("\nNo Superball in your bag")
        elif input_ball == "3":
            clear()
            print("Wild", end=" ")
            print(pokemon_spawn, end=" ")
            print("spawned !")
            if inventory_pokeballs[2][1] > 0:
                inventory_pokeballs[2][1] -= 1
                print("\nHyperball thrown")
                select_pokeball = True
                if random.randint(0, 100) <= catch_chance:
                    pokemons[pokemon_spawn_index][4] += 1
                    for i in range (0, len(inventory_pokemons)):
                        if inventory_pokemons[i][1] != pokemon_spawn:
                            pokemon_different = True
                        else:
                            pokemon_different = False
                            break
                    if pokemon_different == True:
                        inventory_pokemons.append(pokemon_spawn_stats)
                    print(pokemon_spawn,"catched")
                else:
                    print(pokemon_spawn, "escaped")
            else:
                print("\nNo Hyperball in your bag")
        elif input_ball == "4":
            clear()
            print("Wild", end=" ")
            print(pokemon_spawn, end=" ")
            print("spawned !")
            if inventory_pokeballs[3][1] > 0:
                inventory_pokeballs[3][1] -= 1
                print("\nMasterball thrown")
                select_pokeball = True
                pokemons[pokemon_spawn_index][4] += 1
                for i in range (0, len(inventory_pokemons)):
                    if inventory_pokemons[i][1] != pokemon_spawn:
                        pokemon_different = True
                    else:
                        pokemon_different = False
                        break
                if pokemon_different == True:
                    inventory_pokemons.append(pokemon_spawn_stats)
                print(pokemon_spawn, "catched")
            else:
                print("\nNo Masterball in your bag")
        elif input_ball == "":
            clear()
            # select_pokeball = True
            play()
        else:
            clear()
            select_pokeball = True
            catch()
    print("\nEnter: Continue")
    input_continue = input()
    if input_continue == "" or input_continue:
        play()


#   Inventory function - allow player to keep Pokemons and Pokeballs

def inventory():
    select_inventory = False

    inventory_pokemons.sort()
    while select_inventory == False:
        print("Choose your inventory:\n")
        print("1: Pokemons | 2: Pokeballs")
        input_inventory = input()
        if input_inventory == "1":
            clear()
            print(">>> Pokemons inventory <<<\n", end="")
            if inventory_pokemons == []:
                print("Any Pokemon")
            for i in range (0, len(inventory_pokemons)):
                print(inventory_pokemons[i][1], "- Amount:", inventory_pokemons[i][4], end="x\n")
            select_inventory = True
        elif input_inventory == "2":
            clear()
            print(">>> Pokeballs inventory <<<\n", end="")
            for i in range (0, len(inventory_pokeballs)):
                print(inventory_pokeballs[i][0], "- Amount:", inventory_pokeballs[i][1], end="x\n")
            select_inventory = True
        elif input_inventory == "":
            clear()
            select_inventory = True
            play()
        else:
            clear()
    print("\nEnter: Continue")
    input_continue = input()
    if input_continue == "" or input_continue:
        play()


#   Shop function - allow player to buy Pokeballs

def pokeshop():
    global balance
    select_pokeshop = False

    while select_pokeshop == False:
        print("What do you want to buy ?\n", end ="")
        print("Balance:", balance, "P$\n")
        print("1: Pokeball -", pokeballs[0][2], "Pokedollars")
        print("2: Superball -", pokeballs[1][2], "Pokedollars")
        print("3: Hyperball -", pokeballs[2][2], "Pokedollars")
        print("4: Masterball -", pokeballs[3][2], "Pokedollars")
        input_shop = input()
        if input_shop == "1":
            clear()
            if balance >= pokeballs[0][2]:
                balance -= 200
                inventory_pokeballs[0][1] += 1
                print("Pokeball bought: -", end="")
                print(pokeballs[0][2], "Pokedollars\n")
            else:
                print("Not enough Pokedollars")
                select_pokeshop = True
        elif input_shop == "2":
            clear()
            if balance >=  pokeballs[1][2]:
                balance -= 600
                inventory_pokeballs[1][1] += 1
                print("Superball bought: -", end="")
                print(pokeballs[1][2], "Pokedollars\n")
            else:
                print("Not enough Pokedollars")
                select_pokeshop = True
        elif input_shop == "3":
            clear()
            if balance >= pokeballs[2][2]:
                balance -= 1200
                inventory_pokeballs[2][1] += 1
                print("Hyperball bought: -", end="")
                print(pokeballs[2][2], "Pokedollars\n")
            else:
                print("Not enough Pokedollars")
                select_pokeshop = True
        elif input_shop == "4":
            clear()
            if balance >= pokeballs[3][2]:
                balance -= 50000
                inventory_pokeballs[3][1] += 1
                print("Masterball bought: -", end="")
                print(pokeballs[3][2], "Pokedollars\n")
            else:
                print("Not enough Pokedollars")
                select_pokeshop = True
        elif input_shop == "":
            clear()
            select_pokeshop = True
            play()
        else:
            clear()
    print("\nEnter: Continue")
    input_continue = input()
    if input_continue == "" or input_continue:
        play()


#   Pokedex function - displays catched pokemons

def pokedex():
    pokemon_inventory_index = 0
 
    inventory_pokemons.sort()
    print("ID  |  Pokemon")
    for i in range (0, len(inventory_pokemons)):
        pokemon_inventory = inventory_pokemons[i][1]
        inventory_pokemons_index = i
        for i in range (0, len(pokemons)-1):
            if pokemon_inventory == pokemons[i][1]:
                pokemon_inventory_index = i+1
                break
        if pokemon_inventory_index < 9:
            print(pokemon_inventory_index, '  | ', pokemon_inventory, end=" - ")
            print("Attack:", inventory_pokemons[inventory_pokemons_index][5], end=" / ")
            print("Defense:", inventory_pokemons[inventory_pokemons_index][6])
        elif pokemon_inventory_index > 98:
            print(pokemon_inventory_index, '| ', pokemon_inventory, end=" - ")
            print("Attack:", inventory_pokemons[inventory_pokemons_index][5], end=" / ")
            print("Defense:", inventory_pokemons[inventory_pokemons_index][6])
        else:
            print(pokemon_inventory_index, ' | ', pokemon_inventory, end=" - ")
            print("Attack:", inventory_pokemons[inventory_pokemons_index][5], end=" / ")
            print("Defense:", inventory_pokemons[inventory_pokemons_index][6])
    print("\nEnter: Continue")
    input_continue = input()
    if input_continue == "" or input_continue:
        play()


#   Play function - group every functions to play

def play():
    play = True

    clear()
    print("Select a menu:\n", end="")
    print("1: Spawn | 2: Inventory | 3: Shop | 4: Pokedex | Enter: Exit")
    input_play = input()
    while play:
        if input_play == "1":
            clear()
            spawn()
        elif input_play == "2":
            clear()
            inventory()
        elif input_play == "3":
            clear()
            pokeshop()
        elif input_play == "4":
            clear()
            pokedex()
        else:
            clear()
            exit()
            

play()