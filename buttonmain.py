import pygame
import button

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
pygame.display.set_caption("Main Menu")

#Game Variables
game_paused = False


#define fonts
font = pygame.font.SysFont("arialblack", 40)

#define colors
TEXT_COL = (255, 255, 255)

#load button images
#resume_img = pygame.font.SysFont("arialblack", 40)

#create button instances
#resume_img = pygame.image.load("")

def draw_text(text, font, text_col, x, y):
    img= font.render(text, True, text_col)
    screen.blit(img, (x, y))

run = True
while run:

    screen.fill((52, 78, 91))
   #check if game is paused
    if game_paused == True:
     pass
    #display menu
    else:
     draw_text("Press SPACE to pause", font, TEXT_COL, 160, 250)

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
          if event.key == pygame.K_SPACE:
           game_paused == True
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()

pygame.quit() 