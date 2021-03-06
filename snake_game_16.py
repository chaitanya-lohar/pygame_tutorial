# Creating a high Score and displaying it

import pygame
import random
import os

# background sound in game
pygame.mixer.init()

pygame.init()

#colors:
white=(255,255,255)
red=(255,0,0)
black=(0,0,0)
gray=(64,64,64)
green=(77,102,0)
darkgreen=(0,100,0)
darkred=(128,0,0)

screen_width=800
screen_height=600

game_Window=pygame.display.set_mode((screen_width,screen_height))

#background image:
bgimg=pygame.image.load("snake_bg3.jpg")
bgimg=pygame.transform.scale(bgimg,(screen_width,screen_height)).convert_alpha()

#game title
pygame.display.set_caption("Snake Game")


#screen score
font=pygame.font.SysFont(None,50,bold=False,italic=True)
# high score

def text_screen(text,color,x,y):
    screen_text=font.render(text,True,color)
    game_Window.blit(screen_text,[x,y])


def plot_snake(game_window,color,snake_list,snake_size):

    for x,y in snake_list:
        pygame.draw.rect(game_Window,color, [x,y, snake_size, snake_size])

clock = pygame.time.Clock()

def welcome_screen():
    exit_game=False
    while exit_game!=True:

        img = pygame.image.load("game_begin.jpg")
        img = pygame.transform.scale(img, (screen_width, screen_height)).convert_alpha()
        game_Window.fill(green)
        game_Window.blit(img,(0,0))
        text_screen("Welcome to Snake",white,230,210)
        text_screen("Press Space Bar To Play!",red,200,250)
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                exit_game=True
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_SPACE:
                    pygame.mixer.music.load("On.mp3")
                    pygame.mixer.music.play()
                    gameloop()

        pygame.display.update()
        clock.tick(60)

#  game loop:
def gameloop():
    # Game specific variable:
    high_score=0
    game_over = False
    exit_game = False
    snake_x = 40
    snake_y = 50
    snake_size = 20
    velocity_x = 0
    velocity_y = 0
    score = 0
    init_velocity = 5

    food_x = random.randint(20, screen_width / 2)
    food_y = random.randint(20, screen_height / 2)
    food_size = 20

    fps = 60


    snake_list = []
    snake_length = 1
    if(not os.path.exists("high_score.txt")):
        with open("high_score.txt","w") as f:
            f.write("0")

    with open("high_score.txt", "r") as f:
        high_score = f.read()
        # print(high_score)

    while(exit_game!=True):

        # game over
        if game_over == True:
            with open("high_score.txt", "w") as f:
                f.write(str(high_score))
            bimg = pygame.image.load("game_over.jpg")
            bimg = pygame.transform.scale(bimg, (screen_width, screen_height)).convert_alpha()
            game_Window.fill(gray)
            game_Window.blit(bimg,(0,0))
            text_screen("Game Over!",red,300,200)
            text_screen("Press Enter To Play Again..",red,150,250)
            text_screen("Score: " + str(score), red, 300,300)

            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    exit_game=True

                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_RETURN:
                        welcome_screen()

        else:
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
                score+=10
                snake_length+=5
                pygame.mixer.music.load("beep.mp3")
                pygame.mixer.music.play()
                food_x = random.randint(20, screen_width / 2)
                food_y = random.randint(20, screen_height / 2)

            if score>int(high_score):
                high_score=score

            game_Window.fill(green)
            game_Window.blit(bgimg,(0,0))
            text_screen("Score: " + str(score)+" ,"+" High Score: "+str(high_score), black, 5, 5)   # score on screen
            pygame.draw.rect(game_Window, darkred, [food_x, food_y, food_size, food_size])


            head=[]
            head.append(snake_x)
            head.append(snake_y)
            snake_list.append(head)


            if len(snake_list)>snake_length:
                del snake_list[0]

            if head in snake_list[:-1]:
                pygame.mixer.music.load("crash.mp3")
                pygame.mixer.music.play()
                game_over=True

            if snake_x<0 or snake_x>screen_width or snake_y<0 or snake_y>screen_height:
                pygame.mixer.music.load("crash.mp3")
                pygame.mixer.music.play()
                game_over=True

            # pygame.draw.rect(game_Window, black, [snake_x, snake_y, snake_size, snake_size])

            plot_snake(game_Window,black,snake_list, snake_size)

        pygame.display.update()
        clock.tick(fps)

    pygame.quit()
    quit()

welcome_screen()
