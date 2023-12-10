import time
import random


class Player:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.inventory = []


def start_game():
    print("Welcome to Earth 205!")
    player_name = input("Enter your name: ")
    player = Player(player_name)

    print(f"Hello, {player.name}! Your journey begins.")

    while player.health > 0:
        print("\n1. Explore")
        print("2. Check Inventory")
        print("3. Quit")

        choice = input("Choose an action: ")

        if choice == "1":
            explore(player)
        elif choice == "2":
            check_inventory(player)
        elif choice == "3":
            print("Thanks for playing! Goodbye.")
            break
        else:
            print("Invalid choice. Try again.")


def explore(player):
    print("You embark on a journey through the destroyed Earth...")
    time.sleep(2)


    event = random.choice(["combat", "treasure", "nothing"])

    if event == "combat":
        print("You encounter a fearsome monster!")
        combat(player)
    elif event == "treasure":
        print("You discover a hidden treasure!")
        treasure(player)
    else:
        print("You explore peacefully and find nothing of note.")


def combat(player):

    enemy_health = random.randint(50, 100)

    while player.health > 0 and enemy_health > 0:
        print(f"Your health: {player.health}")
        print(f"Enemy health: {enemy_health}")

        action = input("Choose an action (attack/heal): ")

        if action == "attack":
            damage = random.randint(10, 20)
            enemy_health -= damage
            print(f"You dealt {damage} damage to the monster.")
        elif action == "heal":
            heal_amount = random.randint(5, 10)
            player.health += heal_amount
            print(f"You healed yourself for {heal_amount} health.")
        else:
            print("Invalid action. Try again.")

    if player.health > 0:
        print("You defeated the monster!")

        player.inventory.append("Monster Tooth")
    else:
        print("You were defeated in battle. Game over.")


def treasure(player):

    loot = random.choice(["Sword", "Shield", "Health Potion"])
    print(f"You found a {loot}!")

    player.inventory.append(loot)

def check_inventory(player):
    print("Inventory:")
    for item in player.inventory:
        print(f"- {item}")


start_game()