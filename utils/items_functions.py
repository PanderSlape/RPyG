import utils.game_functions as game_functions
import utils.player_functions as player_functions

def craft_menu(game):
    try:
        while True:
            recipes = game["recipes"]
            options = []
            choices = {}

            for recipe in recipes:
                result = game["items_available"][recipe.split(".")[0]][recipe.split(".")[1]]["name"]
                ingredients = game["recipes"][recipe].split(".")
                ok_for_crafting = True
                list_ingredient = []
                for i in range(0, len(ingredients), 2):
                    if ingredients[i+1] in game["player"]["inventory"][ingredients[i]]["owned"]:
                        list_ingredient.append(game["items_available"][ingredients[i]][ingredients[i+1]]["name"])
                        print(list_ingredient)
                    else:
                        ok_for_crafting = False
                if ok_for_crafting:
                    options.append("You can make "+result+"-make_"+recipe+"-\n\tIt will cost you 1x"+list_ingredient[0]+", 1x"+list_ingredient[1]+", 1x"+list_ingredient[2])
            options.append("Exit crafting -exit")

            for i in range(len(options)):
                print("["+str(i)+"] :\t"+options[i].split("-")[0])
                choices[str(i)] = options[i].split("-")[1]

            userChoice = str(input("\nWhat do you want to do ? "))

            while userChoice not in choices:
                userChoice = str(input("\nWhat do you want to do ? "))

            action = choices[userChoice]

            if action == "exit":
                return game
            else:
                game = craft_item(game, action.split("_")[1])
    except Exception as e:
        print(e)

def craft_item(game, recipe):
    try:
        category = recipe.split(".")[0]
        item = recipe.split(".")[1]
        ingredients = game["recipes"][recipe].split(".")
        for i in range(0, len(ingredients), 2):
            game["player"]["inventory"][ingredients[i]]["owned"][ingredients[i+1]]-=1
            if game["player"]["inventory"][ingredients[i]]["owned"][ingredients[i+1]] == 0:
                del game["player"]["inventory"][ingredients[i]]["owned"][ingredients[i+1]]
        if item not in game["player"]["inventory"][category]["owned"]:
            game["player"]["inventory"][category]["owned"][item] = 1
        else:
            game["player"]["inventory"][category]["owned"][item] += 1
    except Exception as e:
        print(e)

    return game

def get_item(game, category, item):
    print("Gained : "+game["items_available"][category][item]["name"])
    if item not in game["player"]["inventory"][category]["owned"]:
        game["player"]["inventory"][category]["owned"][item] = 1
    else:
        game["player"]["inventory"][category]["owned"][item] += 1

    
    return game

def check_inventory(game):
    while True:
        options = []
        choices = {}
        options.append("List weapons .look_weapons")
        options.append("List potions .look_potions")
        options.append("List armor .look_armor")
        options.append("List miscellaneous .look_misc")
        options.append("Exit inventory .exit")

        for i in range(len(options)):
            print("["+str(i)+"] :\t"+options[i].split(".")[0])
            choices[str(i)] = options[i].split(".")[1]

        userChoice = str(input("\nWhat do you want to do ? "))

        while userChoice not in choices:
            userChoice = str(input("\nWhat do you want to do ? "))

        action = choices[userChoice]

        if action == "exit":
            break

        game = look(game, action.split("_")[1])

    return game

def use_item(game, category, item):
    try:
        game["player"]["inventory"][category]["owned"][item]-=1
        effects = game["items_available"][category][item]["effect"].split(".")
        if "heal" in effects:
            game = player_functions.gain_hp(game, int(effects[effects.index("heal")+1]))
    
        if "poison" in effects:
            game = player_functions.lose_hp(game, int(effects[effects.index("poison")+1]))
    
        if "dice" in effects:
            random = game_functions.dice(game)
            if random == 6:
                game = player_functions.get_effect(game, effects[effects.index("dice")+1])
    
        if game["player"]["inventory"][category]["owned"][item] == 0:
            del game["player"]["inventory"][category]["owned"][item]
    except Exception as e:
        print(e)
    return game

def equip_item(game, category, item):
    try:
        game["player"]["inventory"][category]["equipped"] = item
        print(game["items_available"][category][item]["name"]+" was equipped")
    except Exception as e:
        print(e)
    return game

def look(game, category):
    items_list = game["player"]["inventory"][category]["owned"]
    equip = 0
    if len(game["player"]["inventory"][category]) == 2:
        equip = 1
        equipped_item = game["player"]["inventory"][category]["equipped"]

    options = []
    choices = {}

    for item in items_list:
        if equip == 0:
            options.append("You own "+game["items_available"][category][item]["name"]+" | "+str(game["player"]["inventory"][category]["owned"][item])+"x Use it-use_"+item+"-\t"+game["items_available"][category][item]["description"])
        else:
            options.append("You own "+game["items_available"][category][item]["name"]+" | "+str(game["player"]["inventory"][category]["owned"][item])+"x Equip it-use_"+item+"-\t"+game["items_available"][category][item]["description"])
    options.append("Exit list -exit")

    for i in range(len(options)):
        if len(options[i].split("-")) != 2:
            print("["+str(i)+"] :\t"+options[i].split("-")[0])
            print(options[i].split("-")[2])
        else:
            print("["+str(i)+"] :\t"+options[i].split("-")[0])
        choices[str(i)] = options[i].split("-")[1]

    userChoice = str(input("\nWhat do you want to do ? "))

    while userChoice not in choices:
        userChoice = str(input("\nWhat do you want to do ? "))

    action = choices[userChoice]

    if action == "exit":
        return game

    if equip == 0:
        game = use_item(game, category, action.split("_")[1])
    else:
        game = equip_item(game, category, action.split("_")[1])
    return game