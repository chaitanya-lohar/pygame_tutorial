

import pygame
import random
pygame.init()

#colors:
white=(255,255,255)
red=(255,0,0)
black=(0,0,0)
green=(0,128,0)
darkgreen=(0,100,0)
darkred=(128,0,0)

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
velocity_x=0
velocity_y=0
score=0
init_velocity=5

food_x=random.randint(20,screen_width/2)
food_y=random.randint(20,screen_height/2)
food_size=20

fps=60
clock =pygame.time.Clock()


#  game loop:
while(exit_game!=True):
    for event in pygame.event.get():

        if event.type==pygame.QUIT:
            exit_game=True

        if event.type==pygame.KEYDOWN:   # keydown ka matlb aapne koe key press ki he
            if event.key==pygame.K_RIGHT: # if right ki to ye work hona chahiye
                velocity_x+=init_velocity
                velocity_y=0

            if event.key==pygame.K_LEFT: # if left ki to ye work hona chahiye
                velocity_x-=init_velocity
                velocity_y = 0

            if event.key==pygame.K_UP: # if up ki to ye work hona chahiye
                velocity_y-=init_velocity
                velocity_x=0

            if event.key==pygame.K_DOWN: # if down ki to ye work hona chahiye
                velocity_y+=init_velocity
                velocity_x = 0

    snake_x=snake_x+velocity_x
    snake_y=snake_y+velocity_y

    if abs(snake_x-food_x)<6 and abs(snake_y-food_y)<6:
        score+=1
        print("Score:",score*10)
        food_x = random.randint(20, screen_width / 2)
        food_y = random.randint(20, screen_height / 2)


    game_Window.fill(green)
    pygame.draw.rect(game_Window,black,[snake_x,snake_y,snake_size,snake_size])
    pygame.draw.rect(game_Window,darkred,[food_x,food_y,food_size,food_size])
    pygame.display.update()
    clock.tick(fps)

pygame.quit()
quit()