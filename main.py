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
    # Set target
    target = np.array((100, 150))

    # Start in vertical position
    angles = [0] * NUM_LINKS
    angles[0] = 90

    lengths = [LINK_LENGTH] * NUM_LINKS

    # Setup up pygame screen and clock
    pygame.init()
    pygame.display.set_caption(TITLE)
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()

    # Perform gradient descent until end effector is within threshold
    while get_distance(target, lengths, angles) > MIN_THRESHOLD:
        clock.tick(FPS)
        screen.fill(SCREEN_COLOR)

        # Draw the target
        pg_target = to_pygame(target)
        pygame.draw.rect(screen, TARGET_COLOR, [
                         pg_target[0], pg_target[1], LINK_WIDTH, LINK_WIDTH])

        # Check for user-inputted exit
        for events in pygame.event.get():
            if events.type == QUIT:
                sys.exit(0)

        # Draw the links
        start = np.array((0, 0), dtype=float)
        end = np.array((0, 0), dtype=float)
        rot = 0
        for i in range(len(angles)):
            rot += np.deg2rad(angles[i])
            end[0] += np.cos(rot) * lengths[i]
            end[1] += np.sin(rot) * lengths[i]

            pygame.draw.line(screen, LINK_COLOR, to_pygame(
                start.astype(int)), to_pygame(end.astype(int)), LINK_WIDTH)

            start = end.copy()

        pygame.display.update()

        # Perform 1 pass of gradient descent
        inverse_kin(target, lengths, angles)

    # Pause once gradient descent is complete
    pygame.time.wait(2000)


if __name__ == '__main__':
    main()
