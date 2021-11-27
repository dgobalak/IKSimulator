from config import *
from pygame.locals import*
from link import Link
import sys
import pygame


def to_pygame(coord):
    return (coord[0] + WIDTH/2, (HEIGHT/2 - coord[1]))


def to_cartesian(coord):
    return (coord[0] - WIDTH/2, (HEIGHT/2 - coord[1]))


links = [Link(0, 50)]  # List of links


def main():
    screen = pygame.display.set_mode((WIDTH, WIDTH))
    pygame.mouse.set_pos(to_pygame(links[-1].end.get_coordinate()))
    
    while True:
        screen.fill(SCREEN_COLOR)

        for events in pygame.event.get():
            if events.type == QUIT:
                sys.exit(0)

        for link in links:
            pos = to_cartesian(pygame.mouse.get_pos())
            links[0].move(*pos)
            pygame.draw.line(screen, LINK_COLOR, to_pygame(
                link.start.get_coordinate()), to_pygame(link.end.get_coordinate()), LINE_WIDTH)

        pygame.display.update()


if __name__ == '__main__':
    main()
