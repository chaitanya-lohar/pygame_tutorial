
import pygame
x=pygame.init()

# creating window:
gamewindow=pygame.display.set_mode((1200,500))

pygame.display.set_caption("Killer Snake") # game title

# game specific variable:
exit_game=False
game_over=False

# Creating a game loop:
while(exit_game!=True):
    for event in pygame.event.get():

        if event.type==pygame.QUIT:
            exit_game=True

        if event.type==pygame.KEYDOWN:   # have you pressed key or not?? if yes than go inside else not
            if event.key==pygame.K_RIGHT:
                print("you have pressed right key")

            elif event.key==pygame.K_UP:
                print("you have pressed up key")

            elif event.key==pygame.K_DOWN:
                print("you have pressed down key")

            elif event.key==pygame.K_LEFT:
                print("you have pressed left key")


pygame.quit()
quit()