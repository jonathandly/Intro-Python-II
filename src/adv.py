from room import Room
from player import Player
from item import Item
from item import Food
from item import Gold

# Declare all the rooms


outside = Room("Outside Cave Entrance", "North of you, the cave mount beckons")

foyer = Room(
    "Foyer", """Dim light filters in from the south. Dusty passages run north and east.\n""")

overlook = Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.\n""")

narrow = Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.\n""")

treasure = Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.\n""")


# Link rooms together

foyer.s_to = outside
foyer.n_to = overlook
outside.n_to = foyer
foyer.e_to = narrow
overlook.s_to = foyer
narrow.w_to = foyer
narrow.n_to = treasure
treasure.s_to = narrow

#
# Main
#

# Make a new player object that is currently in the 'outside' room.
new_player = Player('jd', outside)
# print(new_player)
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


def check_dir(direction, room):
    # room['n_to'] vs room.n_to
    if hasattr(room, direction) and getattr(room, direction) is not None:
        return getattr(room, direction)
    else:
        print("Not a valid direction")
        return room


exit = False
while not exit:
    current_room = new_player.current_room
    print(current_room)

    choice = input(
        '\nSelect n,s,e, or w to move the player.\nSelect q to exit.\n')
    # try:
    #     if choice == 'q':
    #         exit = True
    #     elif new_player.current_room == room['outside'] and choice == 'n':
    #         new_player.current_room = room['foyer']
    #         print(new_player.current_room)
    #     elif new_player.current_room == room['foyer'] and choice == 's':
    #         new_player.current_room = room['outside']
    #         print(new_player)
    #     elif new_player.current_room == room['foyer'] and choice == 'n':
    #         new_player.current_room = room['overlook']
    #         print(new_player)
    #     elif new_player.current_room == room['foyer'] and choice == 'e':
    #         new_player.current_room = room['narrow']
    #         print(new_player)
    #     elif new_player.current_room == room['overlook'] and choice == 's':
    #         new_player.current_room = room['foyer']
    #         print(new_player)
    #     elif new_player.current_room == room['narrow'] and choice == 'w':
    #         new_player.current_room = room['foyer']
    #         print(new_player)
    #     elif new_player.current_room == room['narrow'] and choice == 'n':
    #         new_player.current_room = room['treasure']
    #         print(new_player)
    #     elif new_player.current_room == room['treasure'] and choice == 's':
    #         new_player.current_room = room['narrow']
    #         print(new_player)
    #     else:
    #         raise NameError('Invalid Selection')
    # except NameError:
    #     print('Error: Please Enter only n,s,e,w or q')

    # check if room exists to west
    if choice == 'q':
        exit = True

    if choice in {'w', 'e', 's', 'n'}:
        new_player.current_room = check_dir(choice + '_to', current_room)

    if choice == 'w':
        if current_room.w_to:
            new_player.current_room = current_room.w_to
    elif choice == 'e':
        if current_room.e_to:
            new_player.current_room = current_room.e_to
    elif choice == 's':
        if current_room.s_to:
            new_player.current_room = current_room.s_to
    elif choice == 'n':
        if current_room.n_to:
            new_player.current_room = current_room.n_to
