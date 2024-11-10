class Character():
    def __init__(self, char_name, char_description): #initialises attributes
        self.name = char_name # creates a character name
        self.description = char_description #creates a character description
        self.conversation = None #this will create dialogue of the character
        #the reason why we dont just put all the attributes in the
        #parent is becuse we want different characters, but they will say diffenrent things
        #inehritance or polymorphism is all about classes being used in different ways.

    def describe(self):#it will describe the characters.
        print (f"{self.name} is in this room!")#  tell what character name is
        print (self.description) #this will describe this character to us

#this set the wording of the character talking to you

    def set_conversation(self, conversation):
        self.conversation = conversation
    
    def talk(self):
        if self.conversation is not None:
            print(f'[{self.name}] says {self.conversation}')
        else:
            print(f"{self.name} + doesn't want to talk to you")

#this method is fight, to have the option to fight

    def fight(self, combat_item): #there is one undefined attribute here, item_combat but it is for the item.py classwhich only a skelelton (not fuctioning yet) so we can create attributes we may come to use later to describe and name items in the game
        print(f"{self.name} + doesnt want to fight you")
        return True

class Friend(Character):
    def __init__(self, char_name, char_description):
        super().__init__(char_name, char_description)
        self.help = None  # Initialize help item to None

    def set_help(self, item_help):
        self.help = item_help  # Set the help item

    def get_help(self):
        return self.help  # Return the help item
    
    def provide_help(self, help_item):
        if help_item == self.help:
            print(f"You take potion from {self.name} and heal yourself with {help_item}.")
            return True
        else:
            print(f"{self.name} I dont have any Magic Potion left, come back tomorrow.")
            return False

class Enemy(Character):#this must be a child of a class, putting character inside the brackets tells Python that the Enemy class will inherit all of the methods from Character.
        def __init__(self, char_name, char_description):
            super().__init__(char_name, char_description) #to ensure the Enemy inherits the character class attributes
            self.weakness = None
        
        def set_weakness(self, item_weakness):
            self.weakness = item_weakness   # Set the weakness

        def get_weakness(self):
            return self.weakness # Return the weakness
        
        def set_sleep(self, sleep_item):
            self.sleep_item = sleep_item  # Set the item needed to put the enemy to sleep

        def get_sleep(self):
            return self.sleep_item  # Return the sleep item

        def set_bribe(self, bribe_item):
            self.bribe_item = bribe_item  #

        def get_bribe(self):
            return self.bribe_item  # Return the bribe item
        
        def fight(self, combat_item):
            if combat_item == self.weakness:
                print(f"You fend {self.name} off with the {combat_item}.")
                return True
            else:
                print(f"{self.name} crushes you, puny adventurer.")
                return False
            
        def sleep(self, sleep_item):
            if sleep_item == self.sleep_item:  
                print(f"{self.name} has fallen asleep!")
                return True
            else:
                print(f"{self.name} didn't fall asleep. You need a {self.sleep_item}.")
                return False
            
        def bribe(self, bribe_item):
            if bribe_item == self.bribe_item:
                print(f"You bribe {self.name} with the {self.bribe_item}.")
                return True
            else:
                print(f"{self.name} is not interested in that bribe.")
                return False
            
# class Character():
#  # Create a character​ 

#     def __init__(self, char_name, char_description):
#         self.name = char_name
#         self.description = char_description
#         self.conversation = None

#     # Describe this character​

#     def describe(self):
#         print( self.name + " is here!")
#         print( self.description)

#     #Set what this character will say when talked to​

#     def set_conversation(self, conversation):
#         self.conversation = conversation
#     Talk to this character​

#     def talk(self):
#        if self.conversation is not None:
#          print("[" + self.name + " says]: " + self.conversation)
#          else:
#            print(self.name + " doesn't want to talk to you")

#     #Fight with this character​

#     def fight(self, combat_item):
#        print(self.name + " doesn't want to fight with you")
#        return True

#     class Enemy(Character):#this must be a child of a class
#         def__init__(self, chara_name, char_descrition): #this is it own
#             super(.__init(char_name, char_description))# this is a suber constructor used to setup and change a parent class
#             self.weakness = None

#         def set_weakeness(self, item_weakness):
#             self.weakness = item_weakness

#         def get_weakness(self):
#             return self.weakness
        
#         def fight(self, cobat_item):
#             if combat_item == self.weakness:
#                 print(f"you fend {self.name} of with the {combat_item}")
#                 return True
#             else:
#                 print(f"{self.name} crush you, puny adventurer!")
#                 return False
            

