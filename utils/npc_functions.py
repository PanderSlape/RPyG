import utils.game_functions as game_functions
import utils.player_functions as player_functions

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
            game = npc_functions.trade(game, character)

        if action == "exit":
            return game

        return game

    except Exception as e:
        print(e)
