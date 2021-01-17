

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

screen_width=800
screen_height=600

game_Window=pygame.display.set_mode((screen_width,screen_height))

#game title
pygame.display.set_caption("Snake Game")


#screen score
font=pygame.font.SysFont(None,55,bold=False)

def screen_score(text,color,x,y):
    screen_text=font.render(text,True,color)
    game_Window.blit(screen_text,[x,y])


def plot_snake(game_window,color,snake_list,snake_size):

    for x,y in snake_list:
        pygame.draw.rect(game_Window,color, [x,y, snake_size, snake_size])

#  game loop:
def gameloop():
    # Game specific variable:
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
    clock = pygame.time.Clock()

    snake_list = []
    snake_length = 1

    while(exit_game!=True):
        # game over
        if game_over == True:
            game_Window.fill(white)
            screen_score("Game Over! Press Enter To Continue..",red,70,250)

            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    exit_game=True

                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_RETURN:
                        gameloop()

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
                score+=1
                snake_length+=5
                food_x = random.randint(20, screen_width / 2)
                food_y = random.randint(20, screen_height / 2)

            game_Window.fill(green)
            screen_score("Score:" + str(score * 10), black, 5, 5)   # score on screen
            pygame.draw.rect(game_Window, darkred, [food_x, food_y, food_size, food_size])


            head=[]
            head.append(snake_x)
            head.append(snake_y)
            snake_list.append(head)


            if len(snake_list)>snake_length:
                del snake_list[0]

            if head in snake_list[:-1]:
                print(head)
                print(snake_list)
                game_over=True

            if snake_x<0 or snake_x>screen_width or snake_y<0 or snake_y>screen_height:
                game_over=True

            # pygame.draw.rect(game_Window, black, [snake_x, snake_y, snake_size, snake_size])

            plot_snake(game_Window,black,snake_list, snake_size)

        pygame.display.update()
        clock.tick(fps)

    pygame.quit()
    quit()

gameloop()