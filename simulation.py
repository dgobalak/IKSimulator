from config import *
from pygame.locals import*
from link import Link
import sys
import pygame


def to_pygame(coord):
    return (coord[0] + WIDTH/2, (HEIGHT - coord[1]))


def to_cartesian(coord):
    return (coord[0] - WIDTH/2, (HEIGHT - coord[1]))

links = []  # List of links
links.append(Link(0, LINK_LENGTH))

for i in range(1, NUM_LINKS):
    links.append(Link(i, LINK_LENGTH, links[i-1]))


def main():
    screen = pygame.display.set_mode((WIDTH, WIDTH))
    
    while True:
        screen.fill(SCREEN_COLOR)

        for events in pygame.event.get():
            if events.type == QUIT:
                sys.exit(0)

        pos = to_cartesian(pygame.mouse.get_pos())
        for link in links[::-1]:
            link.move(*pos)
            pos = link.start.get_coordinate()
            pygame.draw.line(screen, LINK_COLOR, to_pygame(
                link.start.get_coordinate()), to_pygame(link.end.get_coordinate()), LINK_WIDTH)

        pygame.display.update()


if __name__ == '__main__':
    main()
