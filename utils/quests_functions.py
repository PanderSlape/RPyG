import utils.player_functions as player_functions

def enter_dungeon(game, dungeon_name):
    try:
        dungeon = game["map"]["dungeons"][dungeon_name]
        print(dungeon["description"])
        for level in dungeon["levels"]:
            for enemies in dungeon["levels"][level]:
                game = player_functions.fight(game, enemies)
        return game
    except Exception as e:
        print(e)