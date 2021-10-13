#   Random library
import random

#   Init variables
#   Pokedollars
balance = 0

#   Pokemons list - "name", minSpawn, maxSpawn, %Spawn, nbCatch, attack, defense
pokemons = [
    ["Bulbasaur", 0, 60, 0, 0, 49, 49], ["Charmander", 61, 121, 0, 0, 52, 43], ["Squirtle", 122, 182, 0, 0, 48, 65], ["Caterpie", 183, 263, 0, 0, 30, 35], 
    ["Weedle", 264, 344, 0, 0, 35, 30], ["Pidgey", 345, 425, 0, 0, 45, 40], ["Rattata", 426, 506, 0, 0, 56, 35], ["Spearow", 507, 587, 0, 0, 60, 30], 
    ["Ekans", 588, 658, 0, 0, 60, 44], ["Pikachu", 659, 719, 0, 0, 55, 40], ["Sandshrew", 720, 770, 0, 0, 75, 85], ["Nidoran ♀️", 771, 821, 0, 0, 47, 52], 
    ["Nidoran ♂️", 822, 872, 0, 0, 57, 40], ["Clefairy", 873, 923, 0, 0, 45, 48], ["Vulpix", 924, 974, 0, 0, 41, 40], ["Jigglypuff", 975, 1025, 0, 0, 45, 20], 
    ["Zubat", 1026, 1076, 0, 0, 45, 35], ["Golbat", 1077, 1127, 0, 0, 80, 70], ["Oddish", 1128, 1178, 0, 0, 50, 55], ["Paras", 1179, 1229, 0, 0, 70, 55], 
    ["Venonat", 1230, 1280, 0, 0, 55, 50], ["Diglett", 1281, 1351, 0, 0, 55, 25], ["Meowth", 1352, 1412, 0, 0, 45, 35], ["Psyduck", 1413, 1483, 0, 0, 52, 48], 
    ["Mankey", 1484, 1544, 0, 0, 80, 35], ["Growlithe", 1545, 1605, 0, 0, 70, 45], ["Poliwag", 1606, 1666, 0, 0, 50, 40], ["Abra", 1667, 1727, 0, 0, 20, 15], 
    ["Machop", 1728, 1788, 0, 0, 80, 50], ["Bellsprout", 1789, 1849, 0, 0, 75, 35], ["Tentacool", 1850, 1910, 0, 0, 40, 35], ["Geodude", 1911, 1971, 0, 0, 80, 100], 
    ["Ponyta", 1972, 2032, 0, 0, 85, 55], ["Slowpoke", 2033, 2093, 0, 0, 65, 65], ["Magnemite", 2094, 2154, 0, 0, 35, 70], ["Doduo", 2155, 2215, 0, 0, 85, 45], 
    ["Seel", 2216, 2276, 0, 0, 45, 55], ["Grimer", 2277, 2337, 0, 0, 80, 50], ["Shellder", 2338, 2398, 0, 0, 65, 100], ["Gastly", 2399, 2459, 0, 0, 35, 30], 
    ["Onix", 2460, 2500, 0, 0, 45, 160], ["Drowzee", 2501, 2561, 0, 0, 48, 45], ["Krabby", 2561, 2621, 0, 0, 105, 90], ["Voltorb", 2622, 2682, 0, 0, 30, 50], 
    ["Exeggcute", 2683, 2733, 0, 0, 40, 80], ["Cubone", 2734, 2784, 0, 0, 50, 80], ["Lickitung", 2785, 2845, 0, 0, 55, 75], ["Koffing", 2846, 2906, 0, 0, 65, 95], 
    ["Rhyhorn", 2907, 2967, 0, 0, 85, 95], ["Chansey", 2968, 3028, 0, 0, 5, 5], ["Tangela", 3029, 3089, 0, 0, 55, 115], ["Kangaskhan", 3090, 3140, 0, 0, 95, 80], 
    ["Horsea", 3141, 3201, 0, 0, 40, 70], ["Goldeen", 3202, 3252, 0, 0, 67, 60], ["Seaking", 3253, 3303, 0, 0, 92, 65], ["Staryu", 3304, 3354, 0, 0, 45, 55], 
    ["Mr. Mime", 3355, 3405, 0, 0, 45, 65], ["Scyther", 3406, 3446, 0, 0, 110, 80], ["Jynx", 3447, 3497, 0, 0, 50, 35], ["Electabuzz", 3498, 3558, 0, 0, 83, 57], 
    ["Magmar", 3559, 3619, 0, 0, 95, 57], ["Pinsir", 3620, 3680, 0, 0, 125, 100], ["Tauros", 3681, 3721, 0, 0, 100, 95], ["Magikarp", 3722, 3752, 0, 0, 10, 55], 
    ["Gyarados", 3753, 3773, 0, 0, 125, 79], ["Lapras", 3774, 3794, 0, 0, 85, 80], ["Ditto", 3795, 3845, 0, 0, 48, 48], ["Eevee", 3846, 3926, 0, 0, 55, 50], 
    ["Porygon", 3927, 3977, 0, 0, 60, 70], ["Omanyte", 3978, 4038, 0, 0, 40, 100], ["Kabuto", 4039, 4099, 0, 0, 80, 90], ["Aerodactyl", 4100, 4140, 0, 0, 105, 65], 
    ["Snorlax", 4141, 4181, 0, 0, 110, 65], ["Articuno", 4182, 4192, 0, 0, 85, 100], ["Zapdos", 4193, 4203, 0, 0, 90, 85], ["Moltres", 4204, 4214, 0, 0, 100, 90], 
    ["Dratini", 4215, 4245, 0, 0, 64, 45], ["Dragonair", 4246, 4276, 0, 0, 84, 65], ["Dragonite", 4277, 4297, 0, 0, 134, 95], ["Mewtwo", 4298, 4308, 0, 0, 110, 90], 
    ["Mew", 4309, 4319, 0, 0, 100, 100], ["Vaporeon", 4320, 4380, 0, 0, 65, 60], ["Jolteon", 4381, 4441, 0, 0, 65, 60], ["Pyroli", 4442, 4502, 0, 0, 130, 60], 
    ["Espeon", 4503, 4563, 0, 0, 65, 60], ["Umbreon", 4564, 4624, 0, 0, 65, 110], ["Togepi", 4625, 4695, 0, 0, 20, 65], ["Scizor", 4696, 4736, 0, 0, 130, 100], 
    ["Porygon2", 4737, 4787, 0, 0, 80, 90], ["Raikou", 4788, 4808, 0, 0, 85, 75], ["Entei", 4809, 4829, 0, 0, 115, 85], ["Suicune", 4830, 4850, 0, 0, 75, 115], 
    ["Larvitar", 4851, 4881, 0, 0, 64, 50], ["Pupitar", 4882, 4912, 0, 0, 84, 70], ["Tyranitar", 4913, 4933, 0, 0, 134, 110], ["Lugia", 4934, 4944, 0, 0, 90, 130], 
    ["Ho-Oh", 4945, 4955, 0, 0, 130, 90], ["Celebi", 4956, 4976, 0, 0, 100, 100], ["Latios", 4977, 5007, 0, 0, 90, 80], ["Latias", 5008, 5038, 0, 0, 80, 90]
]

#   Pokeballs list - "name", minCatch, maxCatch, price
pokeballs = [
    ["Pokeball", 0, 30, 200], ["Superball", 0, 50, 600], ["Hyperball", 0, 70, 1200], ["Masterball", 0, 100, 50000]
]

#   Pokeballs inventory - "name", amount
inventory_pokeballs = [
    ["Pokeball", 30], ["Superball", 15],["Hyperball", 500], ["Masterball", 100]
]

#   Pokemons inventory
inventory_pokemons = [
    ["Bulbasaur", 0, 60, 0, 1, 49, 49], ["Charmander", 61, 121, 0, 1, 52, 43], ["Squirtle", 122, 182, 0, 1, 48, 65]
]


#   Spawn function - spawn a pokemon with which the player can interact

def spawn():
    global pokemon_spawn
    global pokemon_spawn_stats
    global pokemon_spawn_index
    total_range = 0

    for i in range (0, len(pokemons)):
        total_range += pokemons[i][2] - pokemons[i][1]
    # print(total_range)    # 4940
    random_pokemon = (random.randint(0, total_range))
    # print(random_pokemon)

    for i in range (0, len(pokemons)-1):
        if random_pokemon >= pokemons[i][1] and random_pokemon <= pokemons[i][2]:
            pokemon_spawn = pokemons[i][0]
            pokemon_spawn_stats = pokemons[i]
            pokemon_spawn_index = i
            print("\nWild", end=" ")
            print(pokemon_spawn, end=" ")
            print("spawned !")
    print("\nChoose your action:\n", end="")
    print("1: Fight | 2: Catch | Enter: Flee")
    input_spawn = input()
    if input_spawn == "1":
        fight()
    elif input_spawn == "2":
        catch()
    else:
        print("You fled")

#   Fight function - allow player to fight Pokemons and win Pokedollars

def fight():
    global balance

    print("\nSelect your Pokemon:\n", end="Enter: Flee\n")
    for i in range (0, len(inventory_pokemons)):
        print("Pokemon", i+1, ":", inventory_pokemons[i][0])
    input_fight = input()
    if input_fight == "":
        play()
    elif int(input_fight) == 0 or int(input_fight) > len(inventory_pokemons):
        print("Select a pokemon")
        fight()
    elif int(input_fight) <= len(inventory_pokemons):
        pokemon_stats = inventory_pokemons[int(input_fight)-1]
        pokemon_fight = inventory_pokemons[int(input_fight)-1][0]
        # print(pokemon_stats)
        # print(pokemon_spawn_stats)
        pokemon_ratio_1 = round((pokemon_stats[5] / pokemon_stats[6])+20)
        pokemon_ratio_2 = round((pokemon_spawn_stats[5] / pokemon_spawn_stats[6])+20)
        # print(pokemon_ratio_1)
        # print(pokemon_ratio_2)
        ratio_range = pokemon_ratio_1 + pokemon_ratio_2
        # print(ratio_range)
        ratio_random = random.randint(0, ratio_range)
        # print(ratio_random)
        print("")
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
            print("Balance:", balance, "Pokedollars\n")
        else:
            print("Enemy >", end=" ")
            print(pokemon_spawn, "attacks")
            print("Your Pokemon >", end=" ")
            print(pokemon_fight, "fainted")


#   Catch function - allow player to catch Pokemons

def catch():
    select_pokeball = 0
    pokemon_different = 0

    while select_pokeball < 1:
        print("\nChoose your pokeball:\n", end="")
        print("1: Pokeball", inventory_pokeballs[0][1], end="")
        print("x | 2: Superball", inventory_pokeballs[1][1], end="")
        print("x | 3: Hyperball", inventory_pokeballs[2][1], end="")
        print("x | 4: Masterball", inventory_pokeballs[3][1], end="x | 5: Shop | Enter: Flee\n")
        input_ball = input()
        catch_chance = random.randint(0, 100)
        # print(catch_chance)
        resistance_chance = random.randint(0, 100)
        # print(resistance_chance)
        if input_ball == "1":
            if inventory_pokeballs[0][1] > 0:
                inventory_pokeballs[0][1] -= 1
                print("Pokeball thrown")
                select_pokeball = 1
                if (pokeballs[0][1] <= catch_chance and pokeballs[0][2] >= catch_chance) and (resistance_chance >= 0 and resistance_chance <= 50):
                    pokemons[pokemon_spawn_index][4] += 1
                    for i in range (0, len(inventory_pokemons)):
                        if inventory_pokemons[i][0] != pokemon_spawn:
                            pokemon_different = 1
                        else:
                            pokemon_different = 0
                    if pokemon_different == 1:
                        inventory_pokemons.append(pokemon_spawn_stats)
                    print(pokemon_spawn, "catched")
                else:
                    print(pokemon_spawn, "escaped")
            else:
                print("No Pokeball in your bag")
        elif input_ball == "2":
            if inventory_pokeballs[1][1] > 0:
                inventory_pokeballs[1][1] -= 1
                print("Superball thrown")
                select_pokeball = 1
                if (pokeballs[1][1] <= catch_chance and pokeballs[1][2] >= catch_chance) and (resistance_chance >= 0 and resistance_chance <= 50):
                    pokemons[pokemon_spawn_index][4] += 1
                    for i in range (0, len(inventory_pokemons)):
                        if inventory_pokemons[i][0] != pokemon_spawn:
                            pokemon_different = 1
                        else:
                            pokemon_different = 0
                    if pokemon_different == 1:
                        inventory_pokemons.append(pokemon_spawn_stats)
                    print(pokemon_spawn, "catched")
                else:
                    print(pokemon_spawn, "escaped")
            else:
                print("No Superball in your bag")
        elif input_ball == "3":
            if inventory_pokeballs[2][1] > 0:
                inventory_pokeballs[2][1] -= 1
                print("Hyperball thrown")
                select_pokeball = 1
                if (pokeballs[2][1] <= catch_chance and pokeballs[2][2] >= catch_chance) and (resistance_chance >= 0 and resistance_chance <= 50):
                    pokemons[pokemon_spawn_index][4] += 1
                    for i in range (0, len(inventory_pokemons)):
                        if inventory_pokemons[i][0] != pokemon_spawn:
                            pokemon_different = 1
                        else:
                            pokemon_different = 0
                    if pokemon_different == 1:
                        inventory_pokemons.append(pokemon_spawn_stats)
                    print(pokemon_spawn,"catched")
                else:
                    print(pokemon_spawn, "escaped")
            else:
                print("No Hyperball in your bag")
        elif input_ball == "4":
            if inventory_pokeballs[3][1] > 0:
                inventory_pokeballs[3][1] -= 1
                print("Masterball thrown")
                select_pokeball = 1
                pokemons[pokemon_spawn_index][4] += 1
                for i in range (0, len(inventory_pokemons)):
                    if inventory_pokemons[i][0] != pokemon_spawn:
                        pokemon_different = 1
                if pokemon_different == 1:
                    inventory_pokemons.append(pokemon_spawn_stats)
                    pokemon_different = 0
                    print(inventory_pokemons)
                else:
                    print(inventory_pokemons)
                print(pokemon_spawn, "catched")
            else:
                print("No Masterball in your bag")
        elif input_ball == "5":
            pokeshop()
        elif input_ball == "":
            print("You fled")
            break


#   Inventory function - allow player to keep Pokemons and Pokeballs

def inventory():
    select_inventory = 0

    while select_inventory < 1:
        print("\nChoose your inventory:\n", end="")
        print("1: Pokemons | 2: Pokeballs")
        input_inventory = input()
        if input_inventory == "1":
            print("\n>>> Pokemons inventory <<<\n", end="")
            if inventory_pokemons == []:
                print("Any Pokemon")
            for i in range (0, len(inventory_pokemons)):
                print(inventory_pokemons[i][0], "- Amount:", inventory_pokemons[i][4], end="x\n")
            select_inventory = 1
        elif input_inventory == "2":
            print("\n>>> Pokeballs inventory <<<\n", end="")
            for i in range (0, len(inventory_pokeballs)):
                print(inventory_pokeballs[i][0], "- Amount:", inventory_pokeballs[i][1], end="x\n")
            select_inventory = 1
        elif input_inventory == "":
            select_inventory = 1
        else:
            print("Select an inventory")


#   Shop function - allow player to buy Pokeballs

def pokeshop():
    global balance
    select_pokeshop = 0

    while select_pokeshop < 1:
        print("\nWhat do you want to buy ?\n", end ="")
        print("Balance:", balance, "P$\n")
        print("1: Pokeball -", pokeballs[0][3], "Pokedollars")
        print("2: Superball -", pokeballs[1][3], "Pokedollars")
        print("3: Hyperball -", pokeballs[2][3], "Pokedollars")
        print("4: Masterball -", pokeballs[3][3], "Pokedollars")
        input_shop = input()
        if input_shop == "1":
            if balance >= pokeballs[0][3]:
                balance -= 200
                inventory_pokeballs[0][1] += 1
                print("Pokeball bought: -", end="")
                print(pokeballs[0][3], "Pokedollars")
            else:
                print("Not enough Pokedollars")
                select_pokeshop = 1
        elif input_shop == "2":
            if balance >=  pokeballs[1][3]:
                balance -= 600
                inventory_pokeballs[1][1] += 1
                print("Superball bought: -", end="")
                print(pokeballs[1][3], "Pokedollars")
            else:
                print("Not enough Pokedollars")
                select_pokeshop = 1
        elif input_shop == "3":
            if balance >= pokeballs[2][3]:
                balance -= 1200
                inventory_pokeballs[2][1] += 1
                print("Hyperball bought: -", end="")
                print(pokeballs[2][3], "Pokedollars")
            else:
                print("Not enough Pokedollars")
                select_pokeshop = 1
        elif input_shop == "4":
            if balance >= pokeballs[3][3]:
                balance -= 50000
                inventory_pokeballs[3][1] += 1
                print("Masterball bought: -", end="")
                print(pokeballs[3][3], "Pokedollars")
            else:
                print("Not enough Pokedollars")
                select_pokeshop = 1
        elif input_shop == "":
            select_pokeshop = 1
        else:
            print("Select an item")


#   Pokedex function - 


#   Play function - group every functions to play

def play():
    play = True
    while play == True:
        print("\nSelect a menu:\n", end="")
        print("1: Spawn | 2: Inventory | 3: Shop | 0: Exit")
        input_play = input()
        if input_play == "1":
            spawn()
        elif input_play == "2":
            inventory()
        elif input_play == "3":
            pokeshop()
        elif input_play == "0":
            play = False
            

play()