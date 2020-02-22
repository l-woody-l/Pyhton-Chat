import pygame as pg

WHITE = (255, 255, 255)
GREY = (66, 66, 66)

def main():
    screen = pg.display.set_mode((640, 480))
    font = pg.font.Font(None, 20)
    clock = pg.time.Clock()
    send_box = pg.Rect((599, 459, 40, 20))
    input_box = pg.Rect(0, 459, 140, 20)
    color_inactive = pg.Color(22, 22, 22)
    color_active = pg.Color(33, 33, 33)
    color = color_inactive
    active = False
    text = ''
    done = False

    while not done:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                done = True
            if event.type == pg.MOUSEBUTTONDOWN:
                # If the user clicked on the input_box rect.
                if input_box.collidepoint(event.pos):
                    # Toggle the active variable.
                    active = not active
                else:
                    active = False
                if send_box.collidepoint(event.pos):
                    if text == '':
                        break
                    else:
                        print(text)
                        text = ''
                # Change the current color of the input box.
                color = color_active if active else color_inactive
            if event.type == pg.KEYDOWN:
                if active:
                    if event.key == pg.K_RETURN:
                        if text == '':
                            break
                        else:
                            print(text)
                            text = ''
                    elif event.key == pg.K_BACKSPACE:
                        text = text[:-1]
                    else:
                        text += event.unicode

        screen.fill(GREY)
        # Render the current text.
        txt_surface = font.render(text, True, WHITE)
        # Resize the box if the text is too long.
        width = max(599, txt_surface.get_width()+10)
        input_box.w = width
        # Blit the text.
        screen.blit(txt_surface, (input_box.x+5, input_box.y+5))
        # Blit the input_box rect.
        pg.draw.rect(screen, color, input_box, 2)
        pg.draw.rect(screen, (255, 255, 255), send_box, 1)

        pg.display.flip()
        clock.tick(30)


if __name__ == '__main__':
    pg.init()
    main()
    pg.quit()