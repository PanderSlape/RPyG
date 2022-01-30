import utils.player_functions as player_functions
import utils.items_functions as items_functions

def enter_dungeon(game, dungeon_name):
    try:
        dungeon = game["map"]["dungeons"][dungeon_name]
        print(dungeon["description"])
        for level in dungeon["levels"]:
            for enemies in dungeon["levels"][level]:
                game = player_functions.fight(game, enemies)

        player_inventory = game["player"]["inventory"]
        for item in dungeon["chest"]:
            if item.split(".")[0] == "money":
                game = player_functions.gain_money(game, item.split(".")[1])
            if item.split(".")[0] == "exp":
                game = player_functions.gain_exp(game, int(item.split(".")[1]))
            else:
                game = items_functions.get_item(game, item.split(".")[0], item.split(".")[1])
        return game
    except Exception as e:
        print(e)