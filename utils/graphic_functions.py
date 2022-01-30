import pygame, sys, json
import utils.player_functions
import utils.game_functions
import utils.items_functions
import utils.map_functions

def setup():
    try:
        pygame.init()
        clock = pygame.time.Clock()
    except Exception as e:
        print(e)
    return clock

#create the display surface
def display(game):
    try:
        pygame.display.set_caption(game["player"]["name"])
        clock = setup()
        #surface principal
        screen = pygame.display.set_mode((1310,710))

        if game["player"]["location"]["detail"] == "":
            map_surface = pygame.Surface((990,490))
            map_surface.fill((20,148,20))
        elif game["player"]["location"]["detail"] == "Lindenvale.inn.lobby":
            map_surface = pygame.Surface((990,490)) and pygame.image.load("img/hall_inn_innkeeper.jpg")
        else:
            map_surface = pygame.Surface((990,490)) and pygame.image.load("img/cities.jpg")        

        choice_surface = pygame.Surface((990,190)) and pygame.image.load("img/choice_background.jpg")

        inventory_surface = pygame.Surface((290,690))
        inventory_surface.fill((137,137,137))

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            screen.fill((0,0,0))
            screen.blit(map_surface,(10,10))
            screen.blit(inventory_surface,(1010,10))
            screen.blit(choice_surface,(10,510))
        
            pygame.display.flip()
            clock.tick(60)

    except Exception as e:
        print(e)

#def menu(game):
    #try:

    #except Exception as e:
        #print(e)

#def info_player(game):
    #try:

    #except Exception as e:
        #print(e)
