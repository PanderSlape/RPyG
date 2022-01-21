def player_init(player):
    """
    Create the character
    """

    attribute_points = 10
    ok = 0

    while ok != 1:
        print("Please set your characters strength points. " + str(attribute_points) + " points left. You'll need to set Magical points")
        player["strength"] = int(input())
        if player["strength"] > 10:
            print("Nope, thats overkill")
        elif player["strength"] < 0:
            print("Nope, thats way too low")
        else:
            ok = 1
    attribute_points = attribute_points - player["strength"]

    ok = 0
    while ok != 1:
        print("Please set your characters ability points. " + str(attribute_points) + " points left")
        player["ability"] = int(input())
        if player["ability"] > attribute_points:
            print("Nope, thats overkill")
        elif player["ability"] < 0:
            print("Nope, thats way too low")
        else:
            ok = 1
    attribute_points = attribute_points - player["ability"]

    print("Please name your characters")
    player["name"] = input()
    if player["name"] == "Nietzsche":
        player["name"] = "Zarathoustra"
    elif player["name"] == "Blood":
        player["name"] = "Caleb"
    elif player["name"] == "Raven":
        player["name"] = "Nevermore"

    return player

def gain_exp(game, exp):
    if game["player"]["exp"] + exp >= 100:
        game["player"]["exp"]+=exp
        game["player"]["exp"]-=100
        game = gain_lvl(game)
    else:
        game["player"]["exp"]+=exp

    return game

def gain_hp(game, hp):
    if game["player"]["hp"] + hp >= 100:
        game["player"]["hp"]=100
    else:
        game["player"]["hp"]+=hp

    return game

def gain_lvl(game):
    game["player"]["lvl"]+=1

    return game
