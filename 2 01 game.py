import pygame as pg
from random import randint as rid

pg.init()

gamedisplay = pg.display.set_mode((500, 500)) 
gamedisplay.fill((0, 0, 0))

def rand_color():
    r = rid(0, 255)
    g = rid(0, 255)
    b = rid(0, 255)

    color = (r, g, b)

    return color

color = (255, 255, 255)

radius = 9

game = True
while game:

    events = pg.event.get()

    for g in events:
        if g.type == pg.QUIT:
            game = False

        if g.type == pg.KEYDOWN:
            if g.key == pg.K_SPACE:
                color = rand_color()

        if g.type == pg.MOUSEBUTTONDOWN:
            if g.button == 4:
                radius += 1
            if g.button == 5:
                radius -= 1


    if pg.mouse.get_pressed()[2]:
        color = (0, 0, 0)

    if pg.mouse.get_pressed()[0]:
        mouse_pl = pg.mouse.get_pos()
        pg.draw.circle(gamedisplay, color, mouse_pl, radius)

    pg.display.update()
