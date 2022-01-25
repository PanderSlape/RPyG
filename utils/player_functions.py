import utils.game_functions as game_functions

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
    try:
        print("Gained : "+str(exp)+" exp")
        if game["player"]["exp"] + exp >= 100:
            game["player"]["exp"]+=exp
            game["player"]["exp"]-=100
            game = gain_lvl(game)
        else:
            game["player"]["exp"]+=exp
    except Exception as e:
        print(type(exp))
        print(e)

    return game

def gain_hp(game, hp):
    try:
        print("Gained : "+str(hp)+" hp")
        if game["player"]["hp"] + hp >= 100:
            game["player"]["hp"]=100
        else:
            game["player"]["hp"]+=hp
    except Exception as e:
        print(type(hp))
        print(e)

    return game

def lose_hp(game, hp):
    try:
        print("Lost : "+str(hp)+" hp")
        if game["player"]["hp"] - hp <= 0:
            game["player"]["hp"] = 0
            game = game_functions.game_over(game)
        else:
            game["player"]["hp"]-=hp
    except Exception as e:
        print(type(hp))
        print(e)

    return game

def gain_lvl(game):
    print("Gained : 1 level")
    game["player"]["lvl"]+=1

    return game

def sleep(game, minutes):
    game = gain_hp(game, 1000000)
    game = gain_exp(game, 15)
    game = game_functions.spend_time(game, minutes)
    return game

def check_money(game, coins):
    if game["player"]["inventory"]["money"] >= coins:
        return True
    else:
        print("You cannot afford it")
        return False

def pay(game, character, coins):
    game["player"]["inventory"]["money"] -= coins
    city = game["player"]["location"]["detail"].split(".")[0]
    game["characters"][character]["inventory"][city]["money"] += coins
    return game
