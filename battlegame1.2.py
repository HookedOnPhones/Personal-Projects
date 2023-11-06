import sys

class Character:
    def __init__ (self, my_name, my_damage, my_hp):
        self.my_name = my_name
        self.my_damage = my_damage
        self.my_hp = my_hp
    def stat_display(self):
        print("Character:", self.my_name)
        print("HP: ", self.my_hp)
        print("Damage: ", self.my_damage, "\n")
    def change_damage(self, my_damage):
        self.my_damage = my_damage
    def change_hp(self, my_hp):
        self.my_hp = my_hp
    def get_name (self):
        return self.my_name

# Prompt for characters
def print_choices():    
    print("Choose your character")
    print("1) wizard")
    print("2) elf")
    print("3) human")
    print("4) orc")
    print("5) Exit")

    
# Prompted for selection
def play():
    choice = input("Selection:").lower()
    if choice == "1" or choice == "wizard":
        playercharacter = Character("wizard", 150, 70)
        print("You chose", str(playercharacter.get_name()))
        playercharacter.stat_display()

    elif choice == "2" or choice == "elf":
        playercharacter = Character("elf", 100, 100)
        print("You chose", str(playercharacter.get_name()))
        playercharacter.stat_display()

    elif choice == "3" or choice == "human":
        playercharacter = Character("human", 20, 150)
        print("You chose", str(playercharacter.get_name()))
        playercharacter.stat_display()

    # elif choice == "4" or choice == "orc":
    #     playercharacter = Character("orc", 350, int(dragon_hp / 2))
    #     print("You chose", playercharacter)

    elif choice == "5" or choice == "exit":
        print("Exiting...")
        sys.exit()

    else:
        print("Unknown character")
    return playercharacter

def battle(playercharacter):
    while True:
        dragon = Character("Dragon", 50, 300)
        dragon.my_hp = dragon.my_hp - playercharacter.my_damage

        print("The", playercharacter.my_name, "damaged the Dragon!")
        print("The Dragon's hitpoints are now: ", dragon.my_hp, "\n")
        
#        if playercharacter.my_name == orc and playercharacter.my_damage > 5:
#            playercharacter.my_damage = int(playercharacter.dragon_hp / 2)

        if dragon.my_hp <= 0:
            print("You won! The Dragon has lost the battle")
            break

        playercharacter.my_hp = playercharacter.my_hp - dragon.my_damage
        print("The Dragon damaged the ", playercharacter.my_name)
        print("The", playercharacter.my_name, "hitpoints are now: ", playercharacter.my_hp, "\n")

        if playercharacter.my_hp <= 0:
            print("You lost!")
            break

while True:
    print_choices()
    playercharacter = play()
    battle(playercharacter)
    print("Play again? Y/N")
    choice = input().lower()
    if choice == "y":
        print("Good Luck!")
    elif choice == "n":
        sys.exit()
    else:
        print("Invalid choice. Please enter 'Y' or 'N'.")
