import utils.game_functions as game_functions
import utils.player_functions as player_functions
import utils.items_functions as items_functions

def start_dialogue(game, character):
    try:
        while True:
            if city := game["player"]["location"]["detail"].split(".")[0] not in game["characters"][character]["dialogue"]:
                dialogue = game["characters"][character]["dialogue"]["general"]
            else:
                dialogue = game["characters"][character]["dialogue"][city]

            print("\n"+character+" says \""+dialogue["0"]["speak"]+"\"\n")
            choices = {}
            for i in range(len(dialogue["0"]["responses"])):
                print("["+str(i)+"] :\t"+dialogue["0"]["responses"][str(i)]["response"])
                choices[str(i)] = dialogue["0"]["responses"][str(i)]["action"]

            userChoice = str(input("\nWhat do you want to say ? "))

            while userChoice not in choices:
                userChoice = str(input("\nWhat do you want to say ? "))

            action = choices[userChoice]

            if action == "exit":
                return game
            elif action.split(".")[0] == "dialogue":
                print(action.split(".")[1])
                game = continue_dialogue(game, character, action.split(".")[1])
            elif action.split(".")[0] == "wait":
                game = game_functions.spend_time(game, int(action.split(".")[1]))
                game = player_functions.gain_hp(game, 20)

    except Exception as e:
        print(e)

def continue_dialogue(game, character, following_dialogue):
    try:
        if city := game["player"]["location"]["detail"].split(".")[0] not in game["characters"][character]["dialogue"]:
            dialogue = game["characters"][character]["dialogue"]["general"]
        else:
            dialogue = game["characters"][character]["dialogue"][city]
        
        print("\n"+character+" says \""+dialogue[following_dialogue]["speak"]+"\"\n")
        choices = {}
        for i in range(len(dialogue[following_dialogue]["responses"])):
            print("["+str(i)+"] :\t"+dialogue[following_dialogue]["responses"][str(i)]["response"])
            choices[str(i)] = dialogue[following_dialogue]["responses"][str(i)]["action"]
    
        userChoice = str(input("\nWhat do you want to say ? "))

        while userChoice not in choices:
            userChoice = str(input("\nWhat do you want to say ? "))

        action = choices[userChoice]
        action = action.split(".")
        if "dialogue" in action:
            game = continue_dialogue(game, character, action.split(".")[1])

        if "wait" in action:
            game = game_functions.spend_time(game, int(action.split(".")[1]))
            game = player_functions.gain_hp(game, 20)

        if "pay" in action:
            can_pay = player_functions.check_money(game, int(action[action.index("pay")+1]))
            if can_pay:
                game = player_functions.pay(game, character, int(action[action.index("pay")+1]))
            else:
                return game

        if "sleep" in action:
            game = player_functions.sleep(game, int(action[action.index("sleep")+1]))

        if "trade" in action:
            game = trade_menu(game, character)

        if action == "exit":
            return game

        return game

    except Exception as e:
        print(e)

def trade_menu(game, character):
    try:
        options = []
        options.append("I want to buy .buy")
        options.append("I want to sell .sell")
        options.append("I want to go .exit")

        choices = {}

        for i in range(len(options)):
            print("["+str(i)+"] :\t"+options[i].split(".")[0])
            choices[str(i)] = options[i].split(".")[1]

        userChoice = str(input("\nWhat do you want to do ? "))

        while userChoice not in choices:
            userChoice = str(input("\nWhat do you want to do ? "))
        
        if choices[userChoice] == "buy":
            game = trade_buy(game, character)
        elif choices[userChoice] == "sell":
            game = trade_sell(game, character)
        else:
            return game
    except Exception as e:
        print(e)

def choose_category():
    try:
        options = []
        choices = {}
        options.append("List weapons .weapons")
        options.append("List potions .potions")
        options.append("List armor .armor")
        options.append("List miscellaneous .misc")
        options.append("Exit inventory .exit")

        print(options)

        for i in range(len(options)):
            print("["+str(i)+"] :\t"+options[i].split(".")[0])
            choices[str(i)] = options[i].split(".")[1]

        userChoice = str(input("\nWhat do you want to do ? "))

        while userChoice not in choices:
            userChoice = str(input("\nWhat do you want to do ? "))

        action = choices[userChoice]

        print(action)

        return action
    except Exception as e:
        print(e)

def give_item(game, character, category, item):
    try:
        print("Sold : "+game["items_available"][category][item]["name"])
        character_inventory = game["characters"][character]["inventory"][game["player"]["location"]["detail"].split(".")[0]][category]
        if item not in character_inventory:
            character_inventory = 1
        else:
            character_inventory += 1

        game["player"]["inventory"][category]["owned"][item]-=1
        if game["player"]["inventory"][category]["owned"][item] == 0:
            del game["player"]["inventory"][category]["owned"][item]

        return game
    except Exception as e:
        print(e)

def look_inventory(game, category, character = "You"):
    if character == "You":
        inventory = game["player"]["inventory"][category]["owned"]
        action = "sell"
    else:
        inventory = game["characters"][character]["inventory"][game["player"]["location"]["detail"].split(".")[0]][category]
        action = "buy"
    
    options = []
    choices = {}

    for item in inventory:
            options.append(character+" own "+game["items_available"][category][item]["name"]+" | "+str(inventory[item])+"x | "+str(game["items_available"][category][item]["price"])+" coins "+action+" it-"+item+"-\t"+game["items_available"][category][item]["description"])
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

    item = choices[userChoice]

    if item == "exit":
        return game

    if action == "buy":
        if player_functions.check_money(game, game["items_available"][category][item]["price"]) == True:
            game = player_functions.pay(game, character, game["items_available"][category][item]["price"])
            game = items_functions.get_item(game, category, item)
        else:
            print("You don't have the money to do so")

    else:
        game = player_functions.gain_money(game, game["items_available"][category][item]["price"])
        game = give_item(game, character, category, item)

    return game


def trade_buy(game, character):
    try:
        while True:
            category = choose_category()
            if category == "exit":
                return game
            game = look_inventory(game, category, character)
    except Exception as e:
        print(e)

def trade_sell(game, character):
    try:
        while True:
            category = choose_category()
            if category == "exit":
                print(game)
                return game
            game = look_inventory(game, category)
    except Exception as e:
        print(e)