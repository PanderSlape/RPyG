from random import randint

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

def spend_time(game, minutes):
    if int(game["game"]["time"]["minutes"])+(minutes%60) >= 60:
        minutes += 60
    game["game"]["time"]["minutes"] = str((int(game["game"]["time"]["minutes"])+(minutes%60)) % 60)
    game["game"]["time"]["hours"] = str((int(game["game"]["time"]["hours"])+(minutes//60)) % 24)
    return game

def action_menu(game):
    try:
        options = []

        if game["player"]["location"]["detail"] == "":
            print("\nYou are located at "+str(game["player"]["location"]["x"])+" toward east and "+str(game["player"]["location"]["y"])+" towards south\n")
            options.append("Travel towards north -go_north")
            options.append("Travel towards east -go_east")
            options.append("Travel towards west -go_west")
            options.append("Travel towards south -go_south")
            options.append("Use inventory -inventory")
            options.append("Craft something -craft")
            for city in game["map"]["cities"]:
                if game["player"]["location"]["x"] == game["map"]["cities"][city]["location"]["x"] and game["player"]["location"]["y"] == game["map"]["cities"][city]["location"]["y"]:
                    options.append("There is a city here, enter-enter_"+city)
            for cults in game["map"]["cult"]:
                if game["player"]["location"]["x"] == game["map"]["cult"][cults]["location"]["x"] and game["player"]["location"]["y"] == game["map"]["cult"][cults]["location"]["y"]:
                    options.append("There is a shrine here, pray-pray_"+cults)
            for dungeon in game["map"]["dungeons"]:
                if game["player"]["location"]["x"] == game["map"]["dungeons"][dungeon]["location"]["x"] and game["player"]["location"]["y"] == game["map"]["dungeons"][dungeon]["location"]["y"]:
                    options.append("There is a dungeon here -dungeon_"+dungeon)

        else:
            place = game["player"]["location"]["detail"].split(".")
            if place[0] in game["map"]["cities"]:
                if len(place) == 1:
                    for buildings in game["map"]["cities"][place[0]]["buildings"]:
                        options.append("You can enter the "+buildings+" -enter_"+buildings+"+lobby")
                    options.append("You can leave the city -leave")
                elif place[2] == "lobby":
                    print("\n"+game["map"]["cities"][place[0]]["buildings"][place[1]]["lobby"]["description_text"]+"\n")
                    for characters in game["map"]["cities"][place[0]]["buildings"][place[1]]["lobby"]["characters_inside"]:
                        options.append("You can speak to "+characters+" -speak_"+characters)
                    options.append("You can leave the building -leave")

            options.append("Use inventory -inventory")
            options.append("Craft something -craft")

        choices = {}

        for i in range(len(options)):
            print("["+str(i)+"] :\t"+options[i].split("-")[0])
            choices[str(i)] = options[i].split("-")[1]

        userChoice = str(input("\nWhat do you want to do ? "))

        while userChoice not in choices:
            userChoice = str(input("\nWhat do you want to do ? "))

        return choices[userChoice]
    
    except Exception as e:
        print(e)

def dice(game):
    game = game
    response = randint(1, 6)
    return response

def game_over(game):
    print("You died")
    exit()