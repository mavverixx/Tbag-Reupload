from character import Character, Enemy
from character import Enemy  # Make sure you import Enemy from character.py

dave = Enemy ("Dave", "A smelly zombie")

dave.describe()

dave = Character("Dave", "A smelly zombie")

dave.set_conversation("Hello there! I am going to join your OOP game very soon")

dave.talk()

Enemy.set_weakness("cheese")

print("What will you fight with?")
fight_with = input()
dave.fight(fight_with)

# dave = Character("Dave", "A smelly Zombie")
# dave.describe()
 
# dave.set.coversation("hi Im Dave and totally wont")
# dave.talk()
# dave.set_weakness("cheese").lower

# print("what will you fight?")
# fight_with = input("Enter item here:> ")
# dave.fight(fight_with)