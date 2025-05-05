import pygame as pg
pg.init()

def input2(prompt):
    screen = pg.display.set_mode((640, 480))
    font = pg.font.Font(None, 32)
    input = ""
    active = False
    done = False

    while not done:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                done = True
            if event.type == pg.MOUSEBUTTONDOWN:
                if input_rect.collidepoint(event.pos):
                    active = not active
                else:
                    active = False
                color = color_active if active else color_inactive
            if event.type == pg.KEYDOWN:
                if active:
                    if event.key == pg.K_RETURN:
                        done = True
                    elif event.key == pg.K_BACKSPACE:
                        input = input[:-1]
                    else:
                        input += event.unicode

        screen.fill((255, 255, 255))
        color_inactive = pg.Color('lightskyblue3')
        color_active = pg.Color('dodgerblue2')
        color = color_active if active else color_inactive
        input_rect = pg.Rect(50, 50, 200, 32)
        pg.draw.rect(screen, color, input_rect, 2)

        text_surface = font.render(prompt + input, True, (0, 0, 0))
        screen.blit(text_surface, (input_rect.x + 5, input_rect.y + 5))
        input_rect.w = max(200, text_surface.get_width() + 10)
        pg.display.flip()
        return input


def inputting(message):

    input_box = pg.Rect(100, 100, 200, 30)
    color_inactive = pg.Color('lightskyblue3')
    color_active = pg.Color('dodgerblue2')
    color = color_inactive
    active = False
    text = ''
    done = False

    while not done:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                done = True
            if event.type == pg.MOUSEBUTTONDOWN:
                if input_box.collidepoint(event.pos):
                    active = not active
                else:
                    active = False
                color = color_active if active else color_inactive
            if event.type == pg.KEYDOWN:
                if active:
                    if event.key == pg.K_RETURN:
                        done = True
                    elif event.key == pg.K_BACKSPACE:
                        text = text[:-1]
                    else:
                        text += event.unicode

        screen.fill((255, 255, 255))
        pg.draw.rect(screen, color, input_box, 2)

        txt_surface = font.render(text, True, (0, 0, 0))
        width = max(200, txt_surface.get_width()+10)
        input_box.w = width
        screen.blit(txt_surface, (input_box.x+5, input_box.y+5))
        pg.display.flip()
    return text

input2("Username: ")