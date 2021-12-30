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