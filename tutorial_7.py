

import pygame

pygame.init()

#colors:
white=(255,255,255)
red=(255,0,0)
black=(0,0,0)
green=(0,128,0)
darkgreen=(0,100,0)

screen_width=1200
screen_height=600

game_Window=pygame.display.set_mode((screen_width,screen_height))

#game title
pygame.display.set_caption("Snake Game")

# Game specific variable:
game_over=False
exit_game=False
snake_x=40
snake_y=50
snake_size=20

fps=30
clock =pygame.time.Clock()



#  game loop:
while(exit_game!=True):
    for event in pygame.event.get():

        if event.type==pygame.QUIT:
            exit_game=True

        if event.type==pygame.KEYDOWN:   # keydown ka matlb aapne koe key press ki he
            if event.key==pygame.K_RIGHT: # if right ki to ye work hona chahiye
                snake_x+=10

            if event.key==pygame.K_LEFT: # if left ki to ye work hona chahiye
                snake_x-=10

            if event.key==pygame.K_UP: # if up ki to ye work hona chahiye
                snake_y-=10

            if event.key==pygame.K_DOWN: # if down ki to ye work hona chahiye
                snake_y+=10

    game_Window.fill(green)
    pygame.draw.rect(game_Window,black,[snake_x,snake_y,snake_size,snake_size])
    pygame.display.update()
    clock.tick(fps)

pygame.quit()
quit()