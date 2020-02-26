# Course: CS 30
# Period: 4
# Date created: 19/02/07
# Date last modified: 20/02/24
# Name: Mathew Vonk
# Description: Inventory for RPG

#These are the two lists for the RPG
consumables = []
weapons = []
#print statement for showing available weapons
print("Available Weapons : " f'{weapons}')
print("Available Consumables :" f'{consumables}')
print('--------------------------------')
#player picks up Baton and adds to inventory
weapons.append("Police Baton")
#player picks up Tourniquet
consumables.append("Tourniquet")
#print statement to tell player they found Baton
print("You picked up a Police Baton!")
print('--------------------------------')
#print statement to tell player they found Tourniquet
print("You picked up a Tourniquet!")
print('--------------------------------')
#Inserting pistol at the 0 position on the weapons list
weapons.insert(0, "M1911 Pistol")
#print statement to tell player they found Pistol
print("You picked up a M1911 Pistol!")
print('--------------------------------')
#deleting weapon in the 1 spot on the list or the Baton
del weapons[1]
#print statement to tell player they dropped Baton
print("You dropped your Police Baton")
print('--------------------------------')
#print statement telling the player they used a consumable
print("You used consumeable:")
#popping the item so it returns the item name as it is deleted
print(consumables.pop(0))
print('--------------------------------')
#Inserting the knife in the 0 slot in the weapons list
weapons.insert(0, "Knife")
#print statement to tell player they found Knife
print("You picked up a Knife!")
#line that removes the pistol from the weapons list
weapons.remove("M1911 Pistol")
print('--------------------------------')
#print statement telling the player they ran out of bullets and dropped pistol
print("You ran out of bullets for your gun! you dropped it")
print('--------------------------------')
#adding the chains and steel bar to the weapons list
weapons.append("Chains")
weapons.append("Steel Bar")
#letting player know they picked up these new weapons
print("You picked up a Chain and a Steel Bar from a jail cell!")
print('--------------------------------')
#adding bandage to consumables list
consumables.append("Bandage")
#telling player that they found a bandage
print("You found a Bandage!")
print('--------------------------------')
#list printing off current weapons in their inventory
print("Current weapons : ")
print(weapons)
print('--------------------------------')
#list printing off current consumeables in their inventory
print("Current consumables : ")
print(consumables)
print('--------------------------------')
#list printing off current weapons in their inventory sorted alphabetically
print("List of weapons sorted : ")
print(sorted(weapons))
print('--------------------------------')
#list printing off current weapons in their inventory in reverse
weapons.reverse()
print("Weapons printed in reverse :")
print(weapons)
print('--------------------------------')
#command that tells the player how many items are in the inventory
print("Amount of weapons you currently have : ")
print(len(weapons))
print('--------------------------------')
