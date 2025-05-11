# --- Game State ---
inventory = []

rooms = {
    "the bronx":[
        {"name": "Stake", "type": "weapon", "description": "This could come in handy when facing a vampire."},
        {"name": "Cocktail", "type": "drink", "description": "Restores energy and fun."},
        {"name": "Cross necklace", "type": "accessoire", "description": "A little prude, but handy when facing a vampire."},
        {"name": "Highheel", "type": "weapon", "description": "Who loses a single shoe? But the heel is wooden, this could come in handy when facing a vampire."},
    ],
    "the bathroom":[
        {"name": "lipstick", "type": "accessoire", "description": "Looks like someone forgot their lipstick, but it couldn't hurt to put on some color"},
        {"name": "toiletpaper roll", "type": "trash", "description": "No surprise this is here. Don't know how I could use this."},
    ],
    "the backrooms":[
        {"name": "Spike", "type": "vampire", "description": "A tall, British blond man, with sharp teeth and a monstrous face"}
    ]
}

MAX_INVENTORY_SIZE = 5

current_room = "the bronx"
looks = 0

# --- Functions ---

def show_inventory():
    if not inventory:
        print("You don't carry anything with you, better look around and find something.")
    else:
        print("You currently carry:")
        for item in inventory:
            print(f" {item['name']}")

def show_room_items():
    global items
    print(f"You look around in {current_room}:")
    items = rooms[current_room]
    if not items:
        print("There is nothing to find in this room anymore.")
    else:
        for item in items:
            print(f" {item['name']}")

def pick_up(item_name):
    global items
    if len(inventory) >= MAX_INVENTORY_SIZE:
        print("Your pockets and hands are full, maybe put something down before picking something up.")
        return

    for item in items:
        if item['name'].lower() == item_name.lower():
            inventory.append(item)
            items.remove(item)
            print(f"You now carry a {item['name']} with you.")
            return

    print("I haven't seen that here, maybe try something else.")

def drop(item_name):
    global items
    for item in inventory:
        if item['name'].lower() == item_name.lower():
            inventory.remove(item)
            rooms[current_room].append(item)
            print(f"You put the {item['name']} down.")
            return
    print(f"You don't carry a {item_name} on you.")

def use(item_name):
    global looks
    for item in inventory:
        if item['name'].lower() == item_name.lower():
            item_type = item['type']
            name = item['name']

            spike_in_room = any(obj['type'] == "vampire" for obj in rooms[current_room])

            if item_type == "weapon":
                if current_room == "the backrooms" and spike_in_room:
                    print(f"You firmly grip the {name} and walk up to Spike. He backs off a bit. 'Hey love, slowly with that thing—no reason to get stabby.' He jumps out the window and disappears into the darkness.")
                    rooms[current_room] = [i for i in rooms[current_room] if i['type'] != "vampire"]
                else:
                    print(f"You start swinging the {name} around, but there's nothing to stake here.")
            elif item_type == "accessoire":
                print(f"You put on the {name}. You're sure you look good.")
                looks += 1
                if current_room == "the backrooms" and spike_in_room:
                    print("Spike looks at you. 'Getting pretty for me, love?'")
            elif item_type == "drink":
                print(f"You drink your {name}. Tastes good, you can already feel the energy through your veins!")
                if current_room == "the backrooms" and spike_in_room:
                    print("Spike watches, unimpressed. 'Your little cocktail won't help you.'")
            elif item_type == "trash":
                print("It's just trash, don't know what you want to do with that?")
            elif item_type == "vampire":
                print(f"Not sure how you did that... but I'm sure it's better to keep {name} safe and secure in your pocket.")
            else:
                print("Something went wrong, maybe a typo? Try again.")
            return
    print(f"You don't carry a {item_name} on you.")

def examine(item_name):
    for item in inventory:
        if item['name'].lower() == item_name.lower():
            print(f"{item['name']}: {item['description']}")
            return
    for item in rooms[current_room]:
        if item['name'].lower() == item_name.lower():
            print(f"{item['name']}: {item['description']}")
            return
    print("That item isn't here or in your inventory.")

def room_switch():
    global current_room
    global looks

    print("Where do you want to go? Options:", ', '.join(rooms.keys()))
    choice = input("> ").strip().lower()

    for room in rooms:
        if room == choice:
            current_room = room
            print(f"You walk into {room}.")
            if any(i['type'] == 'vampire' for i in rooms[room]) and looks > 0:
                print("Spike raises an eyebrow. 'Well, aren't you looking sharp, love?'")
            return
    print("That's not a place you can go.")

# --- Game Loop ---

def game_loop():
    print("Welcome to the Buffy based Inventory game, you are in the bronx, try to have some fun!")
    print("Type 'help' for a list of commands.")

    while True:
        command = input("\n> ").strip().lower()
        if command == "help":
            print("Commands:")
            print("  inventory         - Show your inventory")
            print("  look              - Look around the room")
            print("  pickup [item]     - Pick up an item")
            print("  drop [item]       - Drop an item")
            print("  use [item]        - Use an item")
            print("  examine [item]    - Examine an item")
            print("  go                - Move to another room")
            print("  quit              - Quit the game")
        elif command == "inventory":
            show_inventory()
        elif command == "look":
            show_room_items()
        elif command.startswith("pickup "):
            item_name = command[7:]
            pick_up(item_name)
        elif command.startswith("drop "):
            item_name = command[5:]
            drop(item_name)
        elif command.startswith("use "):
            item_name = command[4:]
            use(item_name)
        elif command.startswith("examine "):
            item_name = command[8:]
            examine(item_name)
        elif command == "go":
            room_switch()
        elif command == "quit":
            print("Thanks for playing!")
            break
        else:
            print("Unknown command. Type 'help' to see available commands.")

if __name__ == "__main__":
    game_loop()
