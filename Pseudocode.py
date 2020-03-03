# Course: CS 30
# Period: 4
# Date created: 19/02/27
# Date last modified: 20/02/27
# Name: Mathew Vonk
# Description: Pseudocode for RPG

start menu:
    input "what would you like to do?"
    direction:
        1 : "move left"
        2 : "move right"
        3 : "move forwards"
        4 : "move backwards"
        5 : "check inventory"
        6 : "heal"
   end direction
 if health < 0
 end movement
end start menu

start fight:
    print "You are getting attacked, what will you do?"
    while enemy health > 0

    input "Attack or heal?"
    if input is attack:
        -10 enemy health
    else:
        print "You missed"

    elif input is heal:
        +15 health

    elif player health < 0:
        print "Game over, you died"
        input "play again?"
        if input "yes":
            start menu
        else:
            print "Invalid input"

item use:
    input "item in inventory"
    if item is in inventory:
        use the item if it can be used

    else:
        print " Item not in Inventory"

show stats:
    print "health"
    print "room"

else:
    print "what would you like to see?""
