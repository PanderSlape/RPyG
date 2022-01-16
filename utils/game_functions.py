LEVEL_DIFFICULTY = {"0":"Don't hurt me", "1":"Hurt me plenty", "2":"Ultra-violence"}

def difficulty_choice():
    """
    The difficulty selection screen
    """

    print("\n\n[0] : "+LEVEL_DIFFICULTY["0"]+"\n[1] : "+LEVEL_DIFFICULTY["1"]+"\n[2] : "+LEVEL_DIFFICULTY["2"]+"\n\nPlease select the difficulty level : ", end="")
    difficulty = input()
    while difficulty not in LEVEL_DIFFICULTY:
        difficulty = input("Please select the difficulty level : ")
    
    return difficulty

def play_exposition(game):
    print(game["exposition_text"]["exposition"])
    game["exposition_text"]["was_played"] = "True"

def action_menu(game):
    options = []
    if len(game["player"]["location"]["detail"]) == 0:
        for cities in game["map"]["cities"]:
            if player["player"]["location"]["x"] == cities["location"]["x"] and player["player"]["location"]["y"] == cities["location"]["y"]:
                options.append("There is a city here, enter.enter_city")
        for cults in game["map"]["cult"]:
            if player["player"]["location"]["x"] == cities["cult"]["x"] and player["player"]["location"]["y"] == cities["cult"]["y"]:
                options.append("There is a shrine here, pray.pray")
        for cults in game["map"]["dungeon"]:
            if player["player"]["location"]["x"] == cities["dungeon"]["x"] and player["player"]["location"]["y"] == cities["dungeon"]["y"]:
                options.append("There is a dungeon here, dungeon.enter_dungeon")
        options.append("Travel towards north .go_north")
        options.append("Travel towards east .go_east")
        options.append("Travel towards west .go_west")
        options.append("Travel towards south .go_south")
        options.append("Craft something .craft")
    
    else:
        place = game["player"]["location"]["detail"].split(".")
        if place[0] in game["map"]["cities"]:
            if len(place) == 1:
                for buildings in game["map"]["cities"][place[0]]["buildings"]:
                    options.append("You can enter the "+buildings+" .enter_"+buildings+"_lobby")
            elif place[2] == "lobby":
                print("\n"+game["map"]["cities"][place[0]]["buildings"][place[1]]["lobby"]["description_text"]+"\n")
                for characters in game["map"]["cities"][place[0]]["buildings"][place[1]]["lobby"]["characters_inside"]:
                    options.append("You can speak to "+characters+" .speak_"+characters)
            options.append("You can leave the building .leave")


    choices = {}

    for i in range(len(options)):
        print("["+str(i)+"] :\t"+options[i].split(".")[0])
        choices[i] = options[i].split(".")[1]
    
    userChoice = int(input("\nWhat do you want to do ? "))

    while userChoice not in choices:
        userChoice = int(input("\nWhat do you want to do ? "))

    return choices[userChoice]
