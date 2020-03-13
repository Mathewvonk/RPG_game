# Course: CS 30
# Period: 4
# Date created: 19/03/10
# Date last modified: 20/03/12
# Name: Mathew Vonk
# Description: Nested dictonary

characters = {'playable' :{'Al', 'Tommy', 'Scarlett'},
            'enemies' :{'Zombie', 'Undead dog', 'Armored Zombie'}
            }

inventory = {'weapons': {'Brass Knuckles', 'Machete', 'Pistol'},
            'medical items': {'Bandage', 'Med-kit', 'Splint'},
            'food': {'Cookie', 'Water'}
            }

location = {'Jail cell' :
            {'description': 'Old jail cell with a few posters on the walls'},
            'Entrance' :
            {'description': 'Where prisoners used to come into the jail'},
            'Dining hall' :
            {'description': 'Big room stocked with food and some supplies'},
            'Armory' :
            {'description': 'Guards headquarters with a fine assortment of weapons'}
            }
print("----------------------------------------------------------")

print('Playable characters :')
playablecharacters = characters['playable']
for playableCharacters in playablecharacters:
    print(f"- {playableCharacters}")

print("----------------------------------------------------------")

print('Enemy characters :')
enemycharacters = characters['enemies']
for enemyCharacters in enemycharacters:
    print(f"- {enemyCharacters}")

print("----------------------------------------------------------")

print('Available weapons :')
inventoryweapons = inventory['weapons']
for inventoryWeapons in inventoryweapons:
    print(f"- {inventoryWeapons}")

print("----------------------------------------------------------")

print('Avalible medical supplies :')
inventorymeds = inventory['medical items']
for inventoryMeds in inventorymeds:
    print(f"- {inventoryMeds}")

print("----------------------------------------------------------")

print('Avalible food :')
inventoryfood = inventory['food']
for inventoryFood in inventoryfood:
    print(f"- {inventoryFood}")

print("----------------------------------------------------------")

print('Specific locations around the map :')

for place in location:
    description = location[place]['description']
    print(f"-{place} -- {description}")

print("----------------------------------------------------------")
