import pygame as pg
    
sc = pg.display.set_mode((800, 600))

pg.display.set_caption("Tetris")
clock = pg.time.Clock()

x = 400
y = 300

ball = pg.image.load('ball.gif')

run = True
while run:
    clock.tick(30)
    sc.blit(ball,(x,y))
    sc.display.update()


    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False


class shape 
    pygame.spyte.spyte 



def load image

def 