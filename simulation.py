from config import *
from pygame.locals import*
import sys
import pygame


def convert(coord):
    return (coord[0] + WIDTH/2, (HEIGHT/2 - coord[1]))


start = convert((0, 0))
end = convert((0, 50))


def main():
    screen = pygame.display.set_mode((WIDTH, WIDTH))
    screen.fill(SCREEN_COLOR)

    while True:
        for events in pygame.event.get():
            if events.type == QUIT:
                sys.exit(0)

        pygame.draw.line(screen, LINK_COLOR, start, end, LINE_WIDTH)
        pygame.display.flip()


if __name__ == '__main__':
    main()
