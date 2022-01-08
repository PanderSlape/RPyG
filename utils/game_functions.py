LEVEL_DIFFICULTY = {"0":"Don't hurt me", "1":"Hurt me plenty", "2":"Ultra-violence"}

def difficulty_choice():
    """
    The difficulty selection screen
    """

    print("\n\n[0] : "+LEVEL_DIFFICULTY["0"]+"\n[1] : "+LEVEL_DIFFICULTY["1"]+"\n[2] : "+LEVEL_DIFFICULTY["2"]+"\n\nPlease select the difficulty level :")
    difficulty = input()
    while difficulty not in LEVEL_DIFFICULTY:
        print("Please select the difficulty level :")
        difficulty = input()
    
    return difficulty

def play_exposition(game):
    print(game["exposition_text"]["exposition"])
    game["exposition_text"]["was_played"] = "True"

def action_menu(game):
    options = []
    if len(game["player"]["location"]["details"]) == 0:
        for cities in game["map"]["cities"]:
            if player["player"]["location"]["x"] == cities["location"]["x"] and player["player"]["location"]["y"] == cities["location"]["y"]:
                option.append("There is a city here, enter !")
        for cults in game["map"]["cult"]:
            if player["player"]["location"]["x"] == cities["cult"]["x"] and player["player"]["location"]["y"] == cities["cult"]["y"]:
                option.append("There is a shrine here, enter !")
        for cults in game["map"]["dungeon"]:
            if player["player"]["location"]["x"] == cities["dungeon"]["x"] and player["player"]["location"]["y"] == cities["dungeon"]["y"]:
                option.append("There is a dungeon here, enter !")
    
    else: