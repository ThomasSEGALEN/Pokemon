import random

# Créer une liste des pokémons, incluant une chance de spawn (0 - 100%)

# ["Name", minSpawn, maxSpawn, %Spawn, nbSpawn]

pokemons = [
    ["Bulbizarre", 0, 60, 0, 0], ["Salamèche", 61, 121, 0, 0], ["Carapuce", 122, 182, 0, 0], ["Chenipan", 183, 263, 0, 0], ["Aspicot", 264, 344, 0, 0], ["Roucool", 345, 425, 0, 0], 
    ["Rattata", 426, 506, 0, 0], ["Piafabec", 507, 587, 0, 0], ["Abo", 588, 658, 0, 0], ["Pikachu", 659, 719, 0, 0], ["Sabelette", 720, 770, 0, 0], ["Nidoran ♀️", 771, 821, 0, 0], 
    ["Nidoran ♂️", 822, 872, 0, 0], ["Mélofée", 873, 923, 0, 0], ["Goupix", 924, 974, 0, 0], ["Rondoudou", 975, 1025, 0, 0], ["Nosferapti", 1026, 1076, 0, 0], 
    ["Nosferalto", 1077, 1127, 0, 0], ["Mystherbe", 1128, 1178, 0, 0], ["Paras", 1179, 1229, 0, 0], ["Mimitoss", 1230, 1280, 0, 0], ["Taupiqueur", 1281, 1351, 0, 0], 
    ["Miaouss", 1352, 1412, 0, 0], ["Psykokwak", 1413, 1483, 0, 0], ["Férosinge", 1484, 1544, 0, 0], ["Caninos", 1545, 1605, 0, 0], ["Ptitard", 1606, 1666, 0, 0], 
    ["Abra", 1667, 1727, 0, 0], ["Machoc", 1728, 1788, 0, 0], ["Chétiflor", 1789, 1849, 0, 0], ["Tentacool", 1850, 1910, 0, 0], ["Racaillou", 1911, 1971, 0, 0], 
    ["Ponyta", 1972, 2032, 0, 0], ["Ramoloss", 2033, 2093, 0, 0], ["Magnéti", 2094, 2154, 0, 0], ["Doduo", 2155, 2215, 0, 0], ["Otaria", 2216, 2276, 0, 0], ["Tadmorv", 2277, 2337, 0, 0], 
    ["Kokiyas", 2338, 2398, 0, 0], ["Fantominus", 2399, 2459, 0, 0], ["Onix", 2460, 2500, 0, 0], ["Soporifik", 2501, 2561, 0, 0], ["Krabby", 2561, 2621, 0, 0], 
    ["Voltorbe", 2622, 2682, 0, 0], ["Noeunoeuf", 2683, 2733, 0, 0], ["Osselait", 2734, 2784, 0, 0], ["Excelangue", 2785, 2845, 0, 0], ["Smogo", 2846, 2906, 0, 0], 
    ["Rhinocorne", 2907, 2967, 0, 0], ["Leveinard", 2968, 3028, 0, 0], ["Saquedeneu", 3029, 3089, 0, 0], ["Kangourex", 3090, 3140, 0, 0], ["Hypotrempe", 3141, 3201, 0, 0], 
    ["Poissirène", 3202, 3252, 0, 0], ["Poissoroy", 3253, 3303, 0, 0], ["Stari", 3304, 3354, 0, 0], ["M. Mime", 3355, 3405, 0, 0], ["Insécateur", 3406, 3446, 0, 0], 
    ["Lippoutou", 3447, 3497, 0, 0], ["Élektek", 3498, 3558, 0, 0], ["Magmar", 3559, 3619, 0, 0], ["Scarabrute", 3620, 3680, 0, 0], ["Tauros", 3681, 3721, 0, 0], 
    ["Magicarpe", 3722, 3752, 0, 0], ["Léviator", 3753, 3773, 0, 0], ["Lokhlass", 3774, 3794, 0, 0], ["Métamorph", 3795, 3845, 0, 0], ["Évoli", 3846, 3926, 0, 0], 
    ["Porygon", 3927, 3977, 0, 0], ["Amonita", 3978, 4038, 0, 0], ["Kabuto", 4039, 4099, 0, 0], ["Ptéra", 4100, 4140, 0, 0], ["Ronflex", 4141, 4181, 0, 0], 
    ["Artikodin", 4182, 4192, 0, 0], ["Électhor", 4193, 4203, 0, 0], ["Sulfura", 4204, 4214, 0, 0], ["Minidraco", 4215, 4245, 0, 0], ["Draco", 4246, 4276, 0, 0], 
    ["Dracolosse", 4277, 4297, 0, 0], ["Mewtwo", 4298, 4308, 0, 0], ["Mew", 4309, 4319, 0, 0], ["Aquali", 4320, 4380, 0, 0], ["Voltali", 4381, 4441, 0, 0], ["Pyroli", 4442, 4502, 0, 0], 
    ["Mentali", 4503, 4563, 0, 0], ["Noctali", 4564, 4624, 0, 0], ["Togepi", 4625, 4695, 0, 0], ["Cizayox", 4696, 4736, 0, 0], ["Porygon2", 4737, 4787, 0, 0], 
    ["Raikou", 4788, 4808, 0, 0], ["Entei", 4809, 4829, 0, 0], ["Suicune", 4830, 4850, 0, 0], ["Embrylex", 4851, 4881, 0, 0], ["Ymphect", 4882, 4912, 0, 0], 
    ["Tyranocif", 4913, 4933, 0, 0], ["Lugia", 4934, 4944, 0, 0], ["Ho-Oh", 4945, 4955, 0, 0], ["Celebi", 4956, 4976, 0, 0], ["Latios", 4977, 5007, 0, 0], ["Latias", 5008, 5038, 0, 0]
]

# print(pokemons)


# Créer une méthode spawn, qui, en fonction de la chance de spawn, fait spawn un pokémon (affiche son nom)

def spawn():
    total_range = 0

    for i in range (0, len(pokemons)):
        total_range += pokemons[i][2] - pokemons[i][1]
    # print(total_range)    # 4940
    random_pokemon = (random.randint(0, total_range))
    # print(random_pokemon)

    for i in range (0, len(pokemons)-1):
        if random_pokemon >= pokemons[i][1] and random_pokemon <= pokemons[i][2]:
            print(pokemons[i][0])
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


# Faire spawn 1000 pokémons, calculer le % de chaque pokémon spawn

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


# Comparer le % de spawn avec la chance de spawn du pokémon, afficher pour chaque pokémon spawn, s'il y en a eu plus ou moins que la probabilité de spawn initiale

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


# Créer les pokéball (30%), superball (50%), hyperball (70%), masterball (100%). Mettre un % de chance d'attraper le pokemon pour chacune

balls = [
    ["Pokeball", 0, 30], ["Superball", 0, 50], ["Hyperball", 0, 70], ["Masterball", 0, 100]
]

def catch():
    total_range = 0
    select_pokeball = 0

    for i in range (0, len(pokemons)):
        total_range += pokemons[i][2] - pokemons[i][1]
    # print(total_range)    # 4940
    random_pokemon = (random.randint(0, total_range))
    # print(random_pokemon)

    for i in range (0, len(pokemons)-1):
        if random_pokemon >= pokemons[i][1] and random_pokemon <= pokemons[i][2]:
            pokemon_spawn = pokemons[i][0]
            print(pokemon_spawn)
            pokemons[i][4] += 1
            # print(pokemons[i][4])

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


# Ajouter une "résistance" à chaque pokemon, entre 0 et 50%. La résistance est la diminution de la probabilité d'attraper les pokémons
# Attention, la masterball ne prend pas en compte la resistance

def catchResistance():
    total_range = 0
    select_pokeball = 0

    for i in range (0, len(pokemons)):
        total_range += pokemons[i][2] - pokemons[i][1]
    # print(total_range)    # 4940
    random_pokemon = (random.randint(0, total_range))
    # print(random_pokemon)

    for i in range (0, len(pokemons)-1):
        if random_pokemon >= pokemons[i][1] and random_pokemon <= pokemons[i][2]:
            pokemon_spawn = pokemons[i][0]
            print(pokemon_spawn)
            pokemons[i][4] += 1
            # print(pokemons[i][4])

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
                    print("Pokemon catched")
                else:
                    print("Pokemon escaped")
            else:
                print("Pokemon escaped")
        elif input_ball == "2":
            print("Superball thrown")
            select_pokeball = 1
            if balls[1][1] <= catch_chance and balls[1][2] >= catch_chance:
                if resistance_chance >= 0 and resistance_chance <= 50:
                    print("Pokemon catched")
                else:
                    print("Pokemon escaped")
            else:
                print("Pokemon escaped")
        elif input_ball == "3":
            print("Hyperball thrown")
            select_pokeball = 1
            if balls[2][1] <= catch_chance and balls[2][2] >= catch_chance:
                if resistance_chance >= 0 and resistance_chance <= 50:
                    print("Pokemon catched")
                else:
                    print("Pokemon escaped")
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

# catchResistance()


# Mettre en place un inventaire des objets obtenus :
# - 1 inventaire pokemon
# - 1 inventaire pokeballs

inventory_pokeballs = [
    ["Pokeball", 0], ["Superball", 0],["Hyperball", 0], ["Masterball"]
]
inventory_pokemons = [
    ["pokemon1", 0], ["pokemon2", 0], ["pokemon3", 0]
]

def inventory():
    select_inventory = 0

    while select_inventory < 1:
        print("Choose your inventory:\n", end="")
        print("1: Pokemons | 2: Pokeballs")
        input_inventory = input()
        if input_inventory == "1":
            print("Pokemons inventory")
            select_inventory = 1
        elif input_inventory == "2":
            print("Pokeballs inventory")
            select_inventory = 1
        else:
            print("Select an inventory")










inventory()