import numpy as np
import pygame
import sys

from pygame.locals import*
from config import *
from utils import *


# Get point of the end effector
def forward_kin(lengths, angles):
    rot = 0
    point = np.array((0, 0), dtype=float)

    i = 0
    for angle in angles:
        rot += np.deg2rad(angle)
        point[0] += np.cos(rot) * lengths[i]
        point[1] += np.sin(rot) * lengths[i]
        i += 1

    return point


def get_distance(target, lengths, angles):
    end = forward_kin(lengths, angles)
    return np.linalg.norm(target - end)


def get_gradient(target, lengths, angles, i):
    angle = angles[i]
    dist = get_distance(target, lengths, angles)
    angles[i] += DELTA
    dist_plus_delta = get_distance(target, lengths, angles)
    gradient = (dist_plus_delta - dist) / DELTA
    angles[i] = angle
    return gradient


def inverse_kin(target, lengths, angles):
    for i in range(len(angles)):
        gradient = get_gradient(target, lengths, angles, i)
        angles[i] -= LEARNING_RATE * gradient


def main():
    angles = [90, 0, 0, 0]
    lengths = [100, 100, 100, 100]

    pygame.init()
    pygame.display.set_caption(TITLE)
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()

    target = np.array((100, 200))

    while get_distance(target, lengths, angles) > MIN_THRESHOLD:
        clock.tick(FPS)
        screen.fill(SCREEN_COLOR)

        # Draw the target
        pg_target = to_pygame(target)
        pygame.draw.rect(screen, TARGET_COLOR, [
                         pg_target[0], pg_target[1], LINK_WIDTH, LINK_WIDTH])

        for events in pygame.event.get():
            if events.type == QUIT:
                sys.exit(0)

        inverse_kin(target, lengths, angles)

        start = np.array((0, 0), dtype=float)
        end = np.array((0, 0), dtype=float)
        rot = 0
        for i in range(len(angles)):
            rot += np.deg2rad(angles[i])
            end[0] += np.cos(rot) * lengths[i]
            end[1] += np.sin(rot) * lengths[i]

            print(start.astype(int), end.astype(int))

            pygame.draw.line(screen, LINK_COLOR, to_pygame(
                start.astype(int)), to_pygame(end.astype(int)), LINK_WIDTH)

            start = end.copy()

        pygame.display.update()

    pygame.time.wait(2000)


if __name__ == '__main__':
    main()
