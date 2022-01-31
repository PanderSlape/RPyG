import os
import sys

import json

import utils.game_functions as game_functions
import utils.player_functions as player_functions
import utils.items_functions as items_functions
import utils.map_functions as map_functions
import utils.quests_functions as quests_functions
import utils.npc_functions as npc_functions
#import utils.graphic_functions as graphic_functions

GAME_DIR = "./Games_you_can_play/"
LIST_OF_GAMES = [ games for games in os.listdir(GAME_DIR) if os.path.isdir(GAME_DIR+games)==True]
MENU_CHOICE = {"0":"New Game", "1":"Load Save", "2":"Exit"}

def menu():
    """
    The menu of the game
    """

    print("To start the game you must press enter")
    input()

    i = 0
    choices = {}
    for games in LIST_OF_GAMES:
        print("[%i] :\t%s" %(i, games))
        choices[str(i)] = games
        i+=1

    # Ask user for prefered target
    userChoice = str(input("\nPlease choose a game : "))

    # Check if the choice is good
    while userChoice not in choices:
        print("\nThis is not quite right !")
        userChoice = str(input("\nPlease choose a game : "))

    game_to_play = GAME_DIR + choices[userChoice] + "/"
    game_file = choices[userChoice] + ".json"
    game_saves = "saves/"

    menu = input("\n[0] :\t"+MENU_CHOICE["0"]+"\n[1] :\t"+MENU_CHOICE["1"]+"\n[2] :\t"+MENU_CHOICE["2"]+"\n\nPlease choose what to do :")
    while menu not in MENU_CHOICE:
        menu = input("Please choose what to do :")
    
    return menu, game_to_play, game_file, game_saves

def load_game(gamefile):
    with open(gamefile, 'r') as game:
        json_game = json.load(game)
    
    return json_game

def load_save(saves_dir):
    saves_available = os.listdir(saves_dir)
    saves_available.remove("ping")

    i = 0
    choices = {}
    for saves in saves_available:
        print("[%i] :\t%s" %(i, saves))
        choices[str(i)] = saves
        i+=1

    # Ask user for prefered target
    userChoice = str(input("\nPlease choose a save file : "))

    # Check if the choice is good
    while userChoice not in choices:
        print("\nThis is not quite right !")
        userChoice = str(input("\nPlease choose a save file : "))

    game = load_game(saves_dir+choices[userChoice])

    return game

def save_game(saves_dir, game_name, game):

    name_save = game_name+game["player"]["name"]+"_"+game["game"]["time"]["hours"]+"-"+game["game"]["time"]["minutes"]+".json"
    with open(saves_dir+name_save, 'w') as f:
        json.dump(game, f)


if __name__ == '__main__':
    choice = menu()
    if choice[0] == "0":
        game = load_game(choice[1]+choice[2])
        game["game"]["difficutly"] = game_functions.difficulty_choice()
        game["player"] = player_functions.player_init(game["player"])
        ok = 0
        while ok != 1:
            print("Confirm? Yes/No")
            confirm = input()
            if confirm == "Yes":
                ok = 1
            elif confirm == "No":
                player = player_init() 
            else:
                print("Incorrect input")
    elif choice[0] == "1":
        game = load_save(choice[1]+choice[3])
    elif choice[0] == "2":
        print("exiting")
        input()
        exit()
    try:
        #graphic_functions.setup()
        #graphic_functions.display(game)
        os.system("clear")
        if game["exposition_text"]["was_played"] != "True":
            game_functions.play_exposition(game)

        while True:
            action = game_functions.action_menu(game)
            
            if action.split("_")[0] == "speak":
                game = npc_functions.start_dialogue(game, action.split("_")[1])
            elif action.split("_")[0] == "dungeon":
                game = quests_functions.enter_dungeon(game, action.split("_")[1])
            elif action.split("_")[0] == "enter":
                game = map_functions.enter(game, action.split("_")[1])
            elif action.split("_")[0] == "go":
                game = map_functions.go(game, action.split("_")[1])
            elif action.split("_")[0] == "leave":
                game = map_functions.leave(game)
            elif action.split("_")[0] == "pray":
                game = map_functions.pray(game, action.split("_")[1])
            elif action.split("_")[0] == "craft":
                game = items_functions.craft_menu(game)
            elif action.split("_")[0] == "inventory":
                game = items_functions.check_inventory(game)

    except:
        save_game(choice[1], choice[3], game)
