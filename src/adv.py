from room import Room
from player import Player
from item import Item


#Items

torch = Item("torch", "wooden handle with burning fire on one end, carry this item to eluminate your surroundings")
sword = Item("sword", "pointy on one end and used to poke things")
book = Item("book", "old, dusty, and musty book")
coins = Item("coins", "shiny gold coins, but you get the feeling something is not right about them...")

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons", [sword]),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", [torch]),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""", [book]),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""", [coins]),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#

# Make a new player object that is currently in the 'outside' room.
player = Player(input("What is your name hero?   "), room['outside'])
print(f"\nWelcome {player.name}!")
print("""Enter n, s, w, or e to travel in that direction, i to view your inventory, get/take/drop [item], or q to quit""")
print(f"{player.current_room}")

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.   
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.


while True:    
    cmd = input("---> ").split(" ")
    if len(cmd) == 1:
        cmd = cmd[0]
        if cmd == "q":
            print("\nThanks for playing {player.name}! Goodbye!")
            break
        elif cmd in ("n", "s", "e", "w"):
            player.move(cmd)
        elif cmd == "i" or cmd == "inventory":
            print(player.print_inventory())
        else:
            print(f"\n\n-------->'{cmd}' is not a valid command! Please try again    <-------\n\n")   
    elif len(cmd) == 2:
        verb = cmd[0]
        item_name = cmd[1]
        if verb == "get" or verb == "take":            
            if player.current_room.has_item(item_name):
                player.take_item(item_name)                
            else:
                print(f"There is no {item_name} in this room")
        elif verb == "drop":
            if player.has_item(item_name):                
                player.drop_item(item_name)
            else: print(f"There is no {item_name} in your inventory")
        else:
            print(f"\n\n-------->    '{cmd}' is not a valid command! Please try again    <-------\n\n")          
    else:
        print(f"\n\n-------->    '{cmd}' is not a valid command! Please try again    <-------\n\n")      
        
        
        