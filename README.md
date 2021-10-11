# Pokémon

Développé en **Python**.

# Objectifs :

1)	Créer une liste de Pokémons, incluant une chance de spawn (0% - 100%)

2)	Créer une méthode spwan, qui, en fonction de la chance de spawn, fait spawn un Pokémon (affiche son nom)
  
3)	Faire spawn 1000 pokémons, calculer le % de chaque Pokémon spawn
  
4)	Comparer le % de spawn avec la chance de spawn du pokémon
	Afficher pour chaque Pokémon spawn, s'il y en a eu + ou - que la probabilité de spawn initiale
  
5)	Créer les Pokéball (30%), Superball (50%), Hyperball (70%), Masterball (100%)
	Mettre un % de chance d'attraper le Pokémon pour chacune
  
6)	Ajouter une "résistance" à chaque Pokémon, entre 0 et 50%
	La résistance est la diminution de la probabilité d'attraper les Pokémons
	(la masterball de ne prend pas en compte la resistance)
  
7)	Mettre en place un inventaire des objets obtenus :
	- 1 inventaire Pokémons
	- 1 inventaire Pokéballs
  
8)	Ajouter des statistiques par Pokémon (attaque / défense)
  
9)	Mettre en place les combats (pokemon_1 vs pokemon_2) :
	- ratio1 = attaque_pokemon_1 / defense_pokemon_1
	- ratio2 = attaque_pokemon_2 / defense_pokemon_2
	- gagnant = random de 0 à somme(ratio1, ratio2) (même principe que % spawn)
  
10)	Mettre en place les Pokédollars
	Chaque combat gagné rapporte entre 1 et 2000 Pokédollars
  
11) Ajouter un shop, avec les prix suivants : 
	- Pokeball : 200$
	- Superball : 600$
	- Hyperball : 1200$
	- Masterball : 50000$
  
12)	Mettre en place le tout dans un programme en CLI, avec un menu : 
	- Shop
	- Spawn (entraîne capture OU combat (combat entraine le choix d'un de vos pokémon qui va combattre) )
	- Inventaire Pokeballs
	- Inventaire Pokemons
  
  
**__Deadline - 14 octobre à 15h__**