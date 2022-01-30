import utils.game_functions as game_functions
import utils.player_functions as player_functions

def enter(game, place):
    # enter a city or a building
    if len(place.split("-")) != 1:
        game["player"]["location"]["detail"]+="."+place.split("-")[0]+"."+place.split("-")[1]
    else:
        game["player"]["location"]["detail"]+=place
    game = game_functions.spend_time(game, 5)

    return game

def leave(game):
    # leave a city or a building
    if len(game["player"]["location"]["detail"].split(".")) == 1:
        game["player"]["location"]["detail"] = ""
    else:
        game["player"]["location"]["detail"] = game["player"]["location"]["detail"].split(".")[0]
    game = game_functions.spend_time(game, 5)

    return game

def pray(game, cult):
    try:
        if game["map"]["cult"][cult]["uses"] != 0:
            game["map"]["cult"][cult]["uses"]-=1
            game = player_functions.gain_exp(game, 15)
            game = player_functions.gain_hp(game, 15)
            game = game_functions.spend_time(game, 30)
            print("You suddenly feel better.")
        else:
            print("The shrine has lost it's power.")
    except Exception as e:
        print(e)

    return game

def go(game, direction):
    # Move on the map
    if direction =="north":
        game["player"]["location"]["y"]-=1
    if direction =="south":
        game["player"]["location"]["y"]+=1
    if direction =="east":
        game["player"]["location"]["x"]+=1
    if direction =="west":
        game["player"]["location"]["x"]-=1
    game = game_functions.spend_time(game, 15)
    return game