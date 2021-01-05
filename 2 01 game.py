import pygame as pg
from random import randint as rid

pg.init()

gamedisplay = pg.display.set_mode((500, 500)) # назначение размера окна с игрой
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
    # получение событий
    events = pg.event.get()
    # проверка события на команду закрытия программы
    for g in events:
        if g.type == pg.QUIT: # обработка события закрытия
            game = False

        if g.type == pg.KEYDOWN: # рандомный цвет
            if g.key == pg.K_SPACE:
                color = rand_color()

        if g.type == pg.MOUSEBUTTONDOWN: # размер
            if g.button == 4:  # колёсико вверх
                radius += 1
            if g.button == 5:  # колёсико вниз
                radius -= 1


    if pg.mouse.get_pressed()[2]: # ластик
        color = (0, 0, 0)

    if pg.mouse.get_pressed()[0]: # рисование
        mouse_pl = pg.mouse.get_pos()
        pg.draw.circle(gamedisplay, color, mouse_pl, radius)

    pg.display.update()
