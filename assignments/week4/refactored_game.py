# Imports
import time
import random
import os
import sys

def typingPrint(text):
    for character in text:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)


def typingInput(text):
    for character in text:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
    value = input()
    return value


def clearScreen():
    os.system("cls")


# Constants
OGRE_HEALTH = 250
UNICORN_HEALTH = 100

# Global state
weapon_hand = ""
player_name = ""
enemy_name = ""
enemy_health = 0


# Utility Function - returns how much damage was dealt
def calculate_hit(weapon: str) -> int:
    hit = random.randint(0, 101)
    if hit <= 20:
        typingPrint(f"Your {weapon} barely scratched {enemy_name}. ")
    elif hit >= 70:
        typingPrint(f"Your {weapon} hit {enemy_name}'s weak spot! ")
    else:
        typingPrint(f"Your {weapon} hit {enemy_name} successfully. ")
    return hit


# Weapon Choice Scene
def weapon_choice():
    global weapon_hand
    typingPrint("Which weapon will you choose?\n")

    # Sword ASCII
    print("[1]\n"
          "            _\n"
          " _         | |\n"
          "| | _______| |---------------------------------------------\\ \n"
          "|:-)_______|==[]============================================> \n"
          "|_|        | |---------------------------------------------/ \n"
          "           |_|\n")

    time.sleep(1)

    # Wand ASCII
    print(" [2] \n" 
        "__/\__\n"
        "\    /\n"
        "/_  _\ \n"
        "XX\/XX\n"
        " X  X\n" 
        " X  X\n" 
        " X  X\n"
        " X  X\n" 
        " X  X\n" 
        " X  X\n"
        " X  X\n" 
        " X  X\n"
        " X  X\n" 
        " X  X\n"
        " XXXX\n" 
        "X    X\n"
        " XXXX\n" )


    while True:
        try:
            choice = int(typingInput("Please enter 1 or 2: "))
            if choice == 1:
                weapon_hand = "sword"
                typingPrint("You picked up the sword.\n")
                break
            elif choice == 2:
                weapon_hand = "wand"
                typingPrint("You picked up the wand.\n")
                break
            else:
                typingPrint("That's not an Option.\n")
        except ValueError:
            typingPrint("Please only enter numbers, else you can't play and we wouldn't want that.\n")


# Fight Scene
def fighting():
    global enemy_health
    while enemy_health > 0:
        typingInput(f"Describe your {'attack' if weapon_hand == 'sword' else 'spell'}: ")
        hit = calculate_hit(weapon_hand)
        enemy_health -= hit
        typingPrint(f"You dealt {hit} damage. {enemy_name}'s health is now {enemy_health}.\n")
        time.sleep(1)
    typingPrint(f"You have successfully defeated{enemy_name}.\n")
    game_ending1()


# Try Again Options
def try_choice():
    while True:
        try:
            choice = int(typingInput("\nDo you want to\n[1] Go home\n[2] Fight the ogre\nEnter 1 or 2: "))
            if choice == 1:
                typingPrint(f"You go back to the hut, put down your {weapon_hand}, and call it quits for today.")
                game_ending2()
                break
            elif choice == 2:
                typingPrint("You turn around and return to the ogre.")
                fighting()
                break
            else:
                typingPrint("Invalid choice.")
        except ValueError:
            typingPrint("Please enter a number.")


def try_choice2():
    while True:
        try:
            choice = int(typingInput("\nDo you want to\n[1] Go home\n[2] Fight the unicorn\n[3] Approach again\nEnter 1, 2, or 3: "))
            if choice == 1:
                typingPrint(f"You go back to the hut, put down your {weapon_hand}, and call it quits for today.")
                game_ending2()
                break
            elif choice == 2:
                typingPrint("You go back and fight the unicorn.")
                fighting()
                break
            elif choice == 3:
                typingPrint("You carefully come closer, but step on a twig. The unicorn shrieks from the sound and runs away.")
                game_ending3()
                break
            else:
                typingPrint("That's not one of the options I have presented right?")
        except ValueError:
            typingPrint("Do you know what a number is? That wasn't one. Try again. ")


# Game Endings
def play_again():
    while True:
        try:
            choice = int(typingInput("\nDo you want to play again?\n[1] Yes\n[2] No\n"))
            if choice == 1:
                main()
                break
            elif choice == 2:
                typingPrint("Okay, bye!")
                break
            else:
                typingPrint("Enter 1 or 2, there is no other option!")
        except ValueError:
            typingPrint("We are at the end of the game and you still don't know how to type numbers?")


def game_ending1():
    typingPrint(f"\nAfter defeating{enemy_name}, you return home victorious and exhausted from your long fight.\nWhat a great day!\nThank you {player_name} for playing my game :).")
    play_again()


def game_ending2():
    typingPrint(f"\nWhat a frightening a day, but at least you are safe at home now! \nThank you {player_name} for playing my game :)")
    play_again()


def game_ending3():
    typingPrint(f"\nThe unicorn ran away. What a disappointment :(.\nThank you {player_name} for playing.")
    play_again()


def game_ending4():
    typingPrint(f"\nYou befriended the unicorn. A magical day :D!\nThank you {player_name} for playing.")
    play_again()


# Choice of Path Scene
def way_choice():
    global enemy_name, enemy_health
    typingPrint(f"\nWith your {weapon_hand} in hand, you set off on your adventure. After a little walking the path splits into:\n")
    typingPrint("[1] A clear sunny path with a bridge leading over a river\n[2] A bright forest trail with beautiful green trees\n")

    while True:
        try:
            way = int(typingInput("\nPlease enter 1 or 2: "))
            if way == 1:
                enemy_name = " the ogre "
                enemy_health = OGRE_HEALTH
                typingPrint("You walk up to the bridge looking at the beautiful water. Suddenly a haggish ogre appears in front of you.")
                action = typingInput("What do you do?  \n[1] Attack \n[2] Flee\nPlease enter 1 or 2: ")
                if action == "1":
                    fighting()
                elif action == "2":
                    typingPrint("You run back over the bridge, towards your hut.")
                    try_choice()
                else:
                    typingPrint("That's not one of the options!")
                break
            elif way == 2:
                enemy_name = " the unicorn "
                enemy_health = UNICORN_HEALTH
                typingPrint("You enter the forest looking at the beautiful trees surrounding you. Suddenly you see a unicorn just a couple meters away from you.")
                action = typingInput(" \nWhat do you do?\n[1] Attack \n[2] Flee \n[3] Carefully approach\nPlease enter a number from 1-3:  ")
                if action == "1":
                    fighting()
                elif action == "2":
                    typingPrint("You run back through the forest, towards your hut.")
                    try_choice2()
                elif action == "3":
                    typingPrint("You carefully approach the unicorn. Because of your carful steps the unicorn, doesn't get frightened. Once in reach you gently stroke it's back. The unicorn enjoys your presence")
                    game_ending4()
                else:
                    typingPrint("That was not one of the numbers given as an option!")
                break
            else:
                typingPrint("Not the answer I was looking for, try again!")
        except ValueError:
            typingPrint("Enter numbers only.")


# Main Game Function
def main():
    global player_name
    clearScreen()
    typingPrint("Welcome to Maja's Story Adventure Game!\n")
    player_name = typingInput("Please enter your name: ")

    typingPrint("You wake up in a hut deep in a mysterious forest.\n")
    typingPrint("Before heading out, you must choose a weapon...\n")
    weapon_choice()
    way_choice()


if __name__ == "__main__":
    main()
