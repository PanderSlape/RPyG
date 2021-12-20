MENU_CHOICE = {"1":"New Game", "2":"Load Save", "3":"Exit"}
LEVEL_DIFFICULTY = {"1":"Don't hurt me", "2":"Hurt me plenty", "3":"Ultra-violence"}

def menu():
    """
    The menu of the game
    """

    print("To start the game you must press enter")
    input()
    print("Please choose what to do :\n 1. "+MENU_CHOICE["1"]+"\n 2. "+MENU_CHOICE["2"]+"\n 3. "+MENU_CHOICE["3"])
    menu = input()
    while menu not in MENU_CHOICE:
        print("Please choose what to do :\n 1. "+MENU_CHOICE["1"]+"\n 2. "+MENU_CHOICE["2"]+"\n 3. "+MENU_CHOICE["3"])
        menu = input()
    
    return menu

def difficulty_choice():
    """
    The difficulty selection screen
    """

    print("Please select the difficulty level :\n 1. "+LEVEL_DIFFICULTY["1"]+"\n 2. "+LEVEL_DIFFICULTY["2"]+"\n 3. "+LEVEL_DIFFICULTY["3"])
    difficulty = input()
    while difficulty not in LEVEL_DIFFICULTY:
        print("Please select the difficulty level :\n 1. "+LEVEL_DIFFICULTY["1"]+"\n 2. "+LEVEL_DIFFICULTY["2"]+"\n 3. "+LEVEL_DIFFICULTY["3"])
        difficulty = input()
    
    return difficulty

def player_init():
    """
    Create the character
    """

    point_attributs = 10
    ok = 0

    while ok != 1:
        print("Please set your characters strength points. " + str(point_attributs) + " points left. You'll need to set Magical points")
        strength = int(input())
        if strength > 10:
            print("Nope, thats overkill")
        elif strength < 0:
            print("Nope, thats way too low")
        else:
            ok = 1
    point_attributs = point_attributs - strength

    ok = 0
    while ok != 1:
        print("Please set your characters magical points. " + str(point_attributs) + " points left")
        magical = int(input())
        if magical > point_attributs:
            print("Nope, thats overkill")
        elif magical < 0:
            print("Nope, thats way too low")
        else:
            ok = 1
    point_attributs = point_attributs - magical

    print("Please name your characters")
    name = input()
    if name == "Hitler":
        name = "Nope"
    elif name == "Stalin":
        name = "Neither"
    elif name == "Raven":
        name = "Nevermore"
    elif name == "Caleb":
        name = "Free the fucking source code"
    elif name == "Duke":
        name = "Nobody steals our chicks and lives"
    elif name == "McClane":
        name = "Yippee-ki-yay"
    elif name == "Rocky":
        name = "Adriaaaaaaan !!!!!!"
    elif name == "":
        name = "Null"
    print("Your character name is "+name+", your magical stats are "+str(magical)+" and you strength "+str(strength)+".")
    player = {"name":name,
              "magical":magical,
              "strength":strength,
              "location":1,
              "exp":0,
              "lvl":0,
              "hp":100,
              "inventory":{
                  "weapons":{
                      "equipped":0,
                      "unequipped":[]},
                  "healing":{
                      },
                  "armor":{
                      "equipped_head":0,
                      "equiped_torso":0,
                      "equiped_legs":0,
                      "equipped_feet":0
                      }
                  },
              "quest_completed":[]}

    return player

if __name__ == '__main__':
    choice = menu()
    if choice == "1":
        difficulty = difficulty_choice()
        player = player_init()
        ok = 0
        while ok =! 1:
            print("Confirm? Yes/No")
            confirm = input()
            if confirm == "Yes":
                ok = 1
            elif confirm == "No":
                player = player_init()
            else:
                print("Incorrect input")
        save = {"difficulty":difficulty, "player":player}
    elif choice == "2":
        print("not done already sorry")
        input()
        exit()
    elif choice == "3":
        print("exiting")
        input()
        exit()
    game = True
    while game is True:
        print("the game starts")
