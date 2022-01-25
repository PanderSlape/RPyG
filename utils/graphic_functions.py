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
        screen = pygame.display.set_mode((1300,700))

        #surface second
        map_surface = pygame.Surface((1000,500))
        map_surface.fill((80,186,203))
        inventory_surface = pygame.Surface((300,700))
        inventory_surface.fill((137,137,137))
        choice_surface = pygame.Surface((1000,200))
        choice_surface.fill((132,95,61))

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            screen.fill((255,255,255))
            screen.blit(map_surface,(0,0))
            screen.blit(inventory_surface,(1000,0))
            screen.blit(choice_surface,(0,500))

            pygame.draw.line(screen,(0,0,0),(1000,0),(1000,700),7)
            pygame.draw.line(screen,(0,0,0),(0,500),(1000,500),7)
            pygame.draw.line(screen,(0,0,0),(0,0),(0,700),7)
            pygame.draw.line(screen,(0,0,0),(0,0),(1300,0),7)
            pygame.draw.line(screen,(0,0,0),(1300,0),(1300,700),13)
            pygame.draw.line(screen,(0,0,0),(0,700),(1300,700),13)
        
            pygame.display.flip()
            clock.tick(60)
    except Exception as e:
        print(e)
