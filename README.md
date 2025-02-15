# Text-Based Adventure Game

This repository contains a text-based adventure game written in Python. The game challenges players to explore different rooms, interact with characters, solve puzzles, and engage in fun combat scenarios. The project leverages object-oriented principles to create a modular and extendable game experience.

## Table of Contents

- [Overview](#overview)
  - [The Challenge](#the-challenge)
  - [Gameplay Overview](#gameplay-overview)
  - [Screenshot](#screenshot)
  - [Links](#links)
- [My Process](#my-process)
  - [Built With](#built-with)
  - [What I Learned](#what-i-learned)
  - [Continued Development](#continued-development)
  - [Useful Resources](#useful-resources)
- [Author](#author)
- [Acknowledgments](#acknowledgments)

## Overview

### The Challenge

The goal was to build an engaging text-based adventure game that demonstrates strong fundamentals in Python programming and object-oriented design. The game includes various elements such as room navigation, character interactions (friends, enemies), combat scenarios, and item management. Employers and other developers can view the code to understand my approach to design, error-handling, and modular programming.

### Gameplay Overview

Players start in a kitchen and can navigate through various rooms including a dining hall, ballroom, and more. Each room features interactive items and characters:
- **Characters:** Interact, talk, and even engage in battles.
- **Items:** Collect and use items like keys to unlock new areas.
- **Rooms:** Unique challenges such as locked doors that require keys to enter.
- **Combat:** Engage enemies using specific items to win fights.

The game design emphasizes clarity and maintainability, with code split into multiple modules such as `character.py`, `item.py`, `room.py`, and a main game loop in `main.py`.

*Add or update the screenshot above with an image capturing the gameplay. To capture a screenshot, run the game in your terminal and use your preferred tool (such as FireShot) to capture the output.*

### Links

- **Solution URL:** [https://github.com/mavverixx/Text-Base-Adventure-Game-Reupload](https://github.com/mavverixx/Text-Base-Adventure-Game-Reupload)
- **Live Demo:** *Not applicable* (This game is intended to be run locally via command line)

## My Process

### Built With

- Python 3.x for core logic and object-oriented programming
- Modular code structure to separate game components (characters, items, rooms)
- CLI-based user interaction for straightforward gameplay
- Focus on simplicity and clarity in code organization and design

### What I Learned

Working on this project allowed me to:
- Gain deeper insight into object-oriented programming by designing modular classes (e.g., `Character`, `Enemy`, `Friend`, `Room`, `Item`).
- Improve Python coding skills and learn best practices for error handling and code clarity.
- Understand the importance of user interaction design, even in text-based applications, and how to make the user experience engaging through thoughtful prompts and feedback.
  
Example code snippet showcasing class inheritance:

class Character:
    def __init__(self, char_name, char_description):
        self.name = char_name
        self.description = char_description

    def describe(self):
        print(f"{self.name} is in this room!")
        print(self.description)

class Enemy(Character):
    def __init__(self, char_name, char_description):
        super().__init__(char_name, char_description)
        self.weakness = None

    def set_weakness(self, item_weakness):
        self.weakness = item_weakness

    def fight(self, combat_item):
        if combat_item == self.weakness:
            print(f"You fend {self.name} off with the {combat_item}.")
            return True
        else:
            print(f"{self.name} crushes you, puny adventurer.")
            return False

Continued Development
In future iterations, I plan to:

Implement more intricate puzzles and branching storylines.
Enhance the combat mechanics with additional character statistics and abilities.
Integrate a save/load feature so players can resume adventures.
Consider adding a simple graphical interface using libraries such as curses or pygame.

Useful Resources
Real Python Tutorials – For excellent guides on Python best practices.
Python OOP Concepts – Official Python documentation on classes and objects.
Stack Overflow – For community support on debugging and improving code quality.
Author

Contact
[Linkedin]((https://www.linkedin.com/in/rikkihenry/))

Acknowledgments
I would like to thank everyone who supported me during this project, including peers, mentors, and the helpful community on Stack Overflow. Special thanks to those whose projects and tutorials inspired parts of this game design.

Feel free to reach out with any suggestions or improvements!
