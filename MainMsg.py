import pygame

pygame.init()

# RGB colours
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
MAGENTA = (255, 0, 255)
TURQUOISE = (0, 206, 209)

textfont = pygame.font.SysFont('courier new', 36)


def keypress(done):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return True
    return False

def draw_all(screen):
    screen.fill(WHITE)
    Title = textfont.render('Send Massege to Freid! Yeah!', 1, BLACK)
    screen.blit(Title, (85, 20))

if __name__ == "__main__":
    size = (800, 600)
    xpos = 0
    ypos = 0

    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Messager")

done = False
while not done:
    draw_all(screen)
    done = keypress(done)
    pygame.display.flip()