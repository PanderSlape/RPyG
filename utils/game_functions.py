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