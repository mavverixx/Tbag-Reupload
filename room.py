from item import Item  # Import the Item class

class Room:
    def __init__(self, room_name, age, locked=False):  # Default to not locked
        self.name = room_name
        self.description = None
        self.linked_rooms = {}
        self.age = age
        self.character = None
        self.item = None  # New attribute to hold an item in the room
        self.locked = locked  

    def set_item(self, item):  # Method to set an item in the room
        self.item = item

    def get_item(self):  # Method to get the item from the room
        return self.item

    def get_description(self): 
        return self.description

    def set_description(self, room_description):
        self.description = room_description

    def describe(self):
        print(self.description)

    def get_name(self):
        return self.name
    
    def get_age(self):
        return self.age

    def set_age(self,new_age): 
        if new_age >= 0:
            self.age = new_age

    def set_character(self, new_character):
        self.character = new_character

    def get_character(self):
        return self.character

    def link_room(self, room_to_link, direction):
        self.linked_rooms[direction] = room_to_link

    def get_details(self):
        print(f"You are in the {self.name}")
        print("--------------------------------------")
        print(self.description)
        for direction in self.linked_rooms:
            room = self.linked_rooms[direction]
            print(f"The {room.get_name()} is {direction}")

    def lock(self):  # Method to lock the room
        self.locked = True

    def unlock(self):  # Method to unlock the room
        self.locked = False

    def get_is_locked(self):  # Method to check if the room is locked
        return self.locked

    def move(self, direction, inventory):  # Accept player inventory as a parameter
        if direction in self.linked_rooms:
            next_room = self.linked_rooms[direction]
            if next_room.get_is_locked():  # Checks if the next room is locked
                if "Key" in [item.get_name() for item in inventory]: # Checks if the player has the key
                    print(f"You unlocked the {next_room.get_name()} with the key!")
                    next_room.unlock()  # Unlock the room
                else:
                    print(f"The {next_room.get_name()} is locked. You need a key to enter this room.")
                    return self  # Stay in the current room
            return next_room
        else:
            print("You can't go that way!")
            return self

# print(dir(Room))  # This will list all methods and attributes of the Room class