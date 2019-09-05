import os
from room import Room
from player import Player
from item import Item

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}

items = {
    'apple': Item("apple", "It's an apple what more do you want me to say."),
    'torch': Item('torch', "It lights up to help you see."),
    'something': Item('something', "it's something")
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

room['outside'].add_item(items['apple'])

#
# Main
#

# Make a new player object that is currently in the 'outside' room.
player = Player(room['outside'])
player.add_item(items['torch'])
player.current_room.print_items()
player.print_items()

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

# instructions = 'Ready to explore?\nInstructions: Press Press any key to continue (Press q anytime to quit) '

os.system('cls' if os.name == 'nt' else 'clear')
direction = input('Ready to explore? Press any key '
                  'to continue (Press q anytime to quit) ')
# gameplay loop
while not direction == 'q':
    print(f'You are currently {player.current_room.name}\n'
          f'{player.current_room.description}')

    if len(player.current_room.return_items()) > 0:
        print('Items in this room: ')
        player.current_room.print_items()

    direction = input('Which direction would you like to go?\n[n] = '
                      'North\n[e] = East\n[s] = South\n[w] = West\n(Press '
                      'q anytime to quit)\nDirection: ')

    if direction == 'n':
        os.system('cls' if os.name == 'nt' else 'clear')
        if player.current_room.n_to is None:
            print("There's nothing in that direction. Please choose a"
                  "different direction.")
            continue
        player.current_room = player.current_room.n_to

    elif direction == 'e':
        os.system('cls' if os.name == 'nt' else 'clear')
        if player.current_room.e_to is None:
            print("There's nothing in that direction. Please choose a "
                  "different direction.")
            continue
        player.current_room = player.current_room.e_to

    elif direction == 's':
        os.system('cls' if os.name == 'nt' else 'clear')
        if player.current_room.s_to is None:
            print("There's nothing in that direction. Please choose a "
                  "different direction.")
            continue
        player.current_room = player.current_room.s_to

    elif direction == 'w':
        os.system('cls' if os.name == 'nt' else 'clear')
        if player.current_room.w_to is None:
            print("There's nothing in that direction. Please choose a "
                  "different direction.")
            continue
        player.current_room = player.current_room.w_to

    elif direction == 'i':
        os.system('cls' if os.name == 'nt' else 'clear')
        if len(player.return_items()) > 0:
            print(f'Your Inventory: ')
            player.print_items()
        else:
            print("You don't have any items! Look around to find stuff.")

    elif len(direction.split(' ')) > 1:
        direction = direction.split(' ')
        if direction[0] == 'take':
            os.system('cls' if os.name == 'nt' else 'clear')
            if items[direction[1]] in player.current_room.return_items():
                player.current_room.remove_item(items[direction[1]])
                player.add_item(items[direction[1]])
                print(f'Your Inventory: ')
                player.print_items()

        elif direction[0] == 'drop':
            os.system('cls' if os.name == 'nt' else 'clear')
            if items[direction[1]] in player.return_items():
                player.current_room.add_item(items[direction[1]])
                player.remove_item(items[direction[1]])
                print(f'Your Inventory: ')
                player.print_items()

    elif direction == 'q':
        os.system('cls' if os.name == 'nt' else 'clear')
        break

    else:
        print("You're doing it wrong. Please choose a "
              "direction or press 'q' to quit.")
