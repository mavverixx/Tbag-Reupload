from character import Character, Enemy, Friend
from room import Room
from item import Item 

# Room Initialization
kitchen = Room("kitchen", 5, locked=False)  # south
ballroom = Room("ballroom", 0, locked=False)  # 
dining_hall = Room("dining hall", 0, locked=True)  # 

# Setting descriptions for rooms
kitchen.set_description("A dank and dirty room with flies") 
ballroom.set_description("A vast room with a shiny wooden floor")
dining_hall.set_description("A large room with ornate golden decorations")

# Linking rooms
kitchen.link_room(dining_hall, "south")
dining_hall.link_room(kitchen, "north")
dining_hall.link_room(ballroom, "west")
ballroom.link_room(dining_hall, "east")

# a key item
key = Item("Key", "A small rusty key that unlocks a door.")
kitchen.set_item(key)  
player_inventory = []  # List to store items the player collects

# Create and place the key item in the kitchen
key = Item("Key", "A small rusty key that unlocks a door.")
kitchen.set_item(key)

# Enemy character
dave = Enemy("Dave", "A smelly zombie")
dave.set_conversation("Brrlgrh... rgrhl... brains...")
dave.set_weakness("cheese")

# Friendly character
frodo = Friend("Frodo", "A friendly hobbit with magical powers.")
frodo.set_conversation("Welcome! I have some great items for you.")
frodo.set_help("magic potion")

# Set characters in rooms
dining_hall.set_character(dave)  # Dave in the dining hall
ballroom.set_character(frodo)  # Frodo in the ballroom

# Starting position
current_room = kitchen  # This sets the current_room variable to the kitchen object



if kitchen.get_item() is not None:  # Check if there's an item in the kitchen
    print(f"There is a {kitchen.get_item().get_name()} in the kitchen.")  # Output the item names

while True:  # Start of the infinite loop
    print("\n")  # Print a newline
    current_room.get_details()  # Show details of the current room
    
    inhabitant = current_room.get_character()  # Get character in the room
    if inhabitant is not None:
        inhabitant.describe()  # Describe the inhabitant if present

    command = input("> ")  # Prompt for user command

    # Handle movement commands
    if command in ["north", "south", "east", "west"]:
        current_room = current_room.move(command, player_inventory)  # Move based on user input

    # Handle the take key command
    elif command == "take key":
        if current_room.get_item() is not None:  # Check if there's an item in the current room
            player_inventory.append(current_room.get_item())  # Assuming you have a player_inventory list
            print(f"You picked up the {current_room.get_item().get_name()}.")
            current_room.set_item(None)  # Remove the item from the room
            print("Current Inventory:", [item.get_name() for item in player_inventory])
        else:
            print("There's no key here.")

    # Handle the talk command
    elif command == "talk":
        if inhabitant is not None:  # Check if there's an inhabitant to talk to
            inhabitant.talk()  # Call the talk method
        else:
            print("There's no one to talk to.")

    # Handle the take key command
    elif command == "take key":
        if current_room.get_item() is not None:  # Check if there's an item in the current room
            player_inventory.append(current_room.get_item())  # Assuming you have a player_inventory list
            print(f"You picked up the {current_room.get_item().get_name()}.")
            current_room.set_item(None)  # Remove the item from the room
        else:
            print("There's no key here.")

    # Handle the help command
    elif command == "help":
        if inhabitant is not None:  # If there's an inhabitant to help
            help_item = input("What item do you want to use for help? ")  # Prompt for help item
            if inhabitant.provide_help(help_item):  # Call the help method
                print(f"You received health from {inhabitant.name}!")  # Player heals
            else:
                print(f"{inhabitant.name} didn't help you with that item.")  # Handle unhelpful item
        else:
            print("There's no one to help.")

    # Handle the fight command
    elif command == "fight":
        if inhabitant is not None:  # If there's an inhabitant to fight
            combat_item = input("What item do you want to fight with? ")  # Prompt for combat item
            if inhabitant.fight(combat_item):  # Call the fight method
                print(f"You defeated {inhabitant.name}!")  # Player wins
            else:
                print("You lost the fight!")  # Player loses
                print("GAME OVER, YOU LOSE!")  # End game message
                break  # End the game if the player loses
        else:
            print("There's no one to fight.")

    # Handle the sleep command
    elif command == "sleep":
        if inhabitant is not None:  # If there's an inhabitant to put to sleep
            sleep_item = input("What item do you want to tranquilize with? ")  # Prompt for sleep item
            if inhabitant.sleep(sleep_item):  # Call the sleep method
                print(f"You tranquilized {inhabitant.name}!")  # Success message
            else:
                print(f"{inhabitant.name} didn't fall asleep. You need a {inhabitant.sleep_item} to put them to sleep.")  # Provide feedback
        else:
            print("There's no one to put to sleep.")

    else:
        print("Unknown command. Please try again.")  # Handle unrecognized commands

