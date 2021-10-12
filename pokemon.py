import random

# Créer une liste de Pokémons, incluant une chance de spawn (0 - 100%)
# Ajouter des stats par pokémon (attaque / défense)

# ["Name", minSpawn, maxSpawn, %Spawn, nbSpawn, attack, defense]

balance = 0

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

# print(pokemons)


# Créer une méthode spawn, qui, en fonction de la chance de spawn, fait spawn un Pokémon (affiche son nom)

def spawn():
    total_range = 0
    global pokemon_spawn
    global pokemon_spawn_stats

    for i in range (0, len(pokemons)):
        total_range += pokemons[i][2] - pokemons[i][1]
    # print(total_range)    # 4940
    random_pokemon = (random.randint(0, total_range))
    # print(random_pokemon)

    for i in range (0, len(pokemons)-1):
        if random_pokemon >= pokemons[i][1] and random_pokemon <= pokemons[i][2]:
            pokemon_spawn = pokemons[i][0]
            pokemon_spawn_stats = pokemons[i]
            print(pokemon_spawn, end=" ")
            pokemons[i][4] += 1
            # print(pokemons[i][4])

# spawn()


def pokedex():
    percent_spawn = 0

    for i in range (0, len(pokemons)):
        percent_spawn = (((pokemons[i][2] - pokemons[i][1]) / pokemons[99][2])) * 100
        pokemons[i][3] = round(percent_spawn, 2)
    
    print("ID  |  Pokemon")
    for i in range (0, len(pokemons)):
        if i < 9:
            print(i+1, '  | ', pokemons[i][0], end=" - ")
            print(pokemons[i][3], end="")
            print("%")
        elif i > 98:
            print(i+1, '| ', pokemons[i][0], end=" - ")
            print(pokemons[i][3], end="")
            print("%")
        else:
            print(i+1, ' | ', pokemons[i][0], end=" - ")
            print(pokemons[i][3], end="")
            print("%")

# pokedex()


# Faire spawn 1000 Pokémons, calculer le % de chaque Pokémon spawn

def massSpawn():
    total_range = 0
    pokemon_spawn = 0
    spawn_limit = 100

    for i in range (0, len(pokemons)):
        total_range += pokemons[i][2] - pokemons[i][1]
    # print(total_range)    # 4940

    while pokemon_spawn < spawn_limit:
        random_pokemon = (random.randint(0, total_range))
        # print(random_pokemon)
        for i in range (0, len(pokemons)):
            if random_pokemon >= pokemons[i][1] and random_pokemon <= pokemons[i][2]:
                print(pokemons[i][0])
                pokemons[i][4] += 1
                # print(pokemons[i][4])
        pokemon_spawn += 1
    # print(pokemon_spawn)

# massSpawn()


# Comparer le % de spawn avec la chance de spawn du Pokémon, afficher pour chaque Pokémon spawn, s'il y en a eu plus ou moins que la probabilité de spawn initiale

def spawnPercentage():
    total_range = 0
    pokemon_spawn = 0
    spawn_limit = 100
    percent_spawn = 0

    for i in range (0, len(pokemons)):
        total_range += pokemons[i][2] - pokemons[i][1]
    # print(total_range)    # 5150

    while pokemon_spawn < spawn_limit:
        random_pokemon = (random.randint(0, total_range))
        # print(random_pokemon)
        for i in range (0, len(pokemons)):
            if random_pokemon >= pokemons[i][1] and random_pokemon <= pokemons[i][2]:
                percent_spawn = (((pokemons[i][2] - pokemons[i][1]) / pokemons[99][2]))*100
                pokemons[i][3] = percent_spawn
                pokemon_theoretically = (pokemons[i][3] * spawn_limit)/100
                pokemons[i][4] += 1
                print("Pokemon:", pokemons[i][0], "| Spawn:", pokemons[i][4], "| Theoretical spawn:", round(pokemon_theoretically))
                if (pokemons[i][4] >= pokemon_theoretically-2 and pokemons[i][4] <= pokemon_theoretically+2) or pokemons[i][4] == pokemon_theoretically:
                    print("> AVERAGE\n")
                elif pokemons[i][4] > pokemon_theoretically:
                    print("> MORE\n")
                else:
                    print("> LESS\n")
        pokemon_spawn += 1
    # print(pokemon_spawn)

# spawnPercentage()


# Créer les Pokéball (30%), Superball (50%), Hyperball (70%), mMsterball (100%)
# Mettre un % de chance d'attraper le Pokémon pour chacune

balls = [
    ["Pokeball", 0, 30, 200], ["Superball", 0, 50, 600], ["Hyperball", 0, 70, 1200], ["Masterball", 0, 100, 50000]
]

def catch():
    select_pokeball = 0

    while select_pokeball < 1:
        print("Choose your pokeball:\n", end="")
        print("1: Pokeball | 2: Superball | 3: Hyperball | 4: Masterball")
        input_ball = input()
        catch_chance = random.randint(0, 100)
        # print(catch_chance)
        if input_ball == "1":
            print("Pokeball thrown")
            select_pokeball = 1
            if balls[0][1] <= catch_chance and balls[0][2] >= catch_chance:
                print("Pokemon catched")
            else:
                print("Pokemon escaped")
        elif input_ball == "2":
            print("Superball thrown")
            select_pokeball = 1
            if balls[1][1] <= catch_chance and balls[1][2] >= catch_chance:
                print("Pokemon catched")
            else:
                print("Pokemon escaped")
        elif input_ball == "3":
            print("Hyperball thrown")
            select_pokeball = 1
            if balls[2][1] <= catch_chance and balls[2][2] >= catch_chance:
                print("Pokemon catched")
            else:
                print("Pokemon escaped")
        elif input_ball == "4":
            print("Masterball thrown")
            select_pokeball = 1
            if balls[3][1] <= catch_chance and balls[3][2] >= catch_chance:
                print("Pokemon catched")
            else:
                print("Pokemon escaped")
        else:
            print("Select a pokeball")

# catch()


# Ajouter une "résistance" à chaque Pokémon, entre 0 et 50%
# La résistance est la diminution de la probabilité d'attraper les Pokémons
# Attention, la Masterball ne prend pas en compte la résistance

def catchResistance():
    select_pokeball = 0

    while select_pokeball < 1:
        print("Choose your pokeball:\n", end="")
        print("1: Pokeball | 2: Superball | 3: Hyperball | 4: Masterball")
        input_ball = input()
        catch_chance = random.randint(0, 100)
        # print(catch_chance)
        resistance_chance = random.randint(0, 100)
        # print(resistance_chance)
        if input_ball == "1":
            print("Pokeball thrown")
            select_pokeball = 1
            if balls[0][1] <= catch_chance and balls[0][2] >= catch_chance:
                if resistance_chance >= 0 and resistance_chance <= 50:
                    print(pokemon_spawn, "catched")
                else:
                    print(pokemon_spawn, "escaped")
            else:
                print(pokemon_spawn, "escaped")
        elif input_ball == "2":
            print("Superball thrown")
            select_pokeball = 1
            if balls[1][1] <= catch_chance and balls[1][2] >= catch_chance:
                if resistance_chance >= 0 and resistance_chance <= 50:
                    print(pokemon_spawn, "catched")
                else:
                    print(pokemon_spawn, "escaped")
            else:
                print(pokemon_spawn, "escaped")
        elif input_ball == "3":
            print("Hyperball thrown")
            select_pokeball = 1
            if balls[2][1] <= catch_chance and balls[2][2] >= catch_chance:
                if resistance_chance >= 0 and resistance_chance <= 50:
                    print(pokemon_spawn,"catched")
                else:
                    print(pokemon_spawn, "escaped")
            else:
                print(pokemon_spawn, "escaped")
        elif input_ball == "4":
            print("Masterball thrown")
            select_pokeball = 1
            print(pokemon_spawn, "catched")
        else:
            pass

# catchResistance()


# Mettre en place un inventaire des objets obtenus :
# - 1 Inventaire Pokémons
# - 1 Inventaire Pokéballs

inventory_pokeballs = [
    ["Pokeball", 0], ["Superball", 0],["Hyperball", 0], ["Masterball", 0]
]
inventory_pokemons = [
    ["Bulbasaur", 0, 60, 0, 0, 49, 49], ["Charmander", 61, 121, 0, 0, 52, 43], ["Squirtle", 122, 182, 0, 0, 48, 65]
]

def inventory():
    select_inventory = 0

    while select_inventory < 1:
        print("Choose your inventory:\n", end="")
        print("1: Pokemons | 2: Pokeballs")
        input_inventory = input()
        if input_inventory == "1":
            print("--- Pokemons inventory ---")
            if inventory_pokemons == []:
                print("Any Pokemon")
            for i in range (0, len(inventory_pokemons)):
                print("Pokemon:", inventory_pokemons[i][0], "| Amount:", inventory_pokemons[i][1])
            select_inventory = 1
        elif input_inventory == "2":
            print("--- Pokeballs inventory ---")
            for i in range (0, len(inventory_pokeballs)):
                print("Pokeball:", inventory_pokeballs[i][0], "| Amount:", inventory_pokeballs[i][1])
            select_inventory = 1
        else:
            print("Select an inventory")

# inventory()


# Mettre en place les combats (pokemon_1 vs pokemon_2) :
# - ratio1 = attaque_pokemon_1 / defense_pokemon_1
# - ratio2 = attaque_pokemon_2 / defense_pokemon_2
# - gagnant = random de 0 à somme(ratio1, ratio2). (meme principe que % spawn)
# Mettre en place les Pokédollars
# Chaque combat gagné rapporte entre 1 et 2000 Pokédollars

def fight():
    global balance

    print("Select your Pokemon:")
    for i in range (0, len(inventory_pokemons)):
        print("Pokemon", i+1, ":", inventory_pokemons[i][0])
    input_fight = input()
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
        print("Balance:", balance, "Pokedollars")
    else:
        print("Enemy >", end=" ")
        print(pokemon_spawn, "attacks")
        print("Your Pokemon >", end=" ")
        print(pokemon_fight, "fainted")

# fight()


# Ajouter un shop, avec les prix suivants : 
#       -> pokeball : 200$
#       -> superball : 600$
#       -> hyperball : 1 200$
#       -> masterball : 50 000$

def pokeshop():
    global balance

    print("What do you want to buy ?\n", end ="")
    print("Balance:", balance, "P$\n")
    print("1: Pokeball -", balls[0][3], "Pokedollars")
    print("2: Superball -", balls[1][3], "Pokedollars")
    print("3: Hyperball -", balls[2][3], "Pokedollars")
    print("4: Masterball -", balls[3][3], "Pokedollars")
    input_shop = input()
    if input_shop == "1":
        if balance >= balls[0][3]:
            balance -= 200
            inventory_pokeballs[0][1] += 1
            print("Pokeball bought: -", end="")
            print(balls[0][3], "Pokedollars")
        else:
            print("You can not buy this item")
    elif input_shop == "2":
        if balance >=  balls[1][3]:
            balance -= 600
            inventory_pokeballs[1][1] += 1
            print("Superball bought: -", end="")
            print(balls[1][3], "Pokedollars")
        else:
            print("You can not buy this item")
    elif input_shop == "2":
        if balance >= balls[2][3]:
            balance -= 1200
            inventory_pokeballs[2][1] += 1
            print("Hyperball bought: -", end="")
            print(balls[2][3], "Pokedollars")
        else:
            print("You can not buy this item")
    elif input_shop == "2":
        if balance >= balls[3][3]:
            balance -= 50000
            inventory_pokeballs[3][1] += 1
            print("Masterball bought: -", end="")
            print(balls[3][3], "Pokedollars")
        else:
            print("You can not buy this item")

# pokeshop()


def play():
    while True:
        x = input()
        print("Wild", end=" ")
        spawn()
        print("spawned!")
        print("Choose your action:\n", end="")
        print("1: Fight | 2: Catch | 3: Inventory | 4: Shop | Enter: Flee | 0: Exit")
        input_play = input()
        if input_play == "1":
            fight()
        elif input_play == "2":
            catchResistance()
        # elif input_play == "3":   Inventory
        elif input_play == "4":
            pokeshop()
        elif input_play == "0":
            break
        else:
            pass

play()