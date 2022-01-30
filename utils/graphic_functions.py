import pygame, sys

def setup():
    try:
        pygame.init()
        clock = pygame.time.Clock()
    except Exception as e:
        print(e)

#create the display surface
def display(game):
    try:
        pygame.display.set_caption(game["player"]["name"])

        #surface principal
        screen = pygame.display.set_mode((1310,710))


        #surface second
        map_surface = pygame.Surface((990,490))
        map_surface.fill((80,186,203))
        inventory_surface = pygame.Surface((290,690))
        inventory_surface.fill((137,137,137))
        choice_surface = pygame.Surface((990,190)) and pygame.image.load("img/choice_background.jpg")

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

#def update_map(game):
    #try:

    #except Exception as e:
        #print(e)

#def update_choice(choice):
    #try:

    #except Exception as e:
        #print(e)

#def update_inventory(game):
    #try:

    #except Exception as e:
        #print(e)

#def menu(game):
    #try:

    #except Exception as e:
        #print(e)

#def info_player(game):
    #try:

    #except Exception as e:
        #print(e)
