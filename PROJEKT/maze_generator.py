import pygame
import time
import random

BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)

width = 800
height = 550
size = (width, height)

pygame.init()
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Maze generator")
clock = pygame.time.Clock()

grid = []
visited = []
stack = []


def draw_grid():
    y = 0
    cell_w = 25
    for i in range(0, 20):
        x = 25
        y = y + 25
        for j in range(0, 30):
            pygame.draw.line(screen, WHITE, [x, y], [x + cell_w, y])  # gorna krawedz komorki
            pygame.draw.line(screen, WHITE, [x + cell_w, y], [x + cell_w, y + cell_w])  # prawa krawedz
            pygame.draw.line(screen, WHITE, [x, y + cell_w], [x + cell_w, y + cell_w])  # dolna krawedz
            pygame.draw.line(screen, WHITE, [x, y], [x, y + cell_w])  # lewa krawedz
            grid.append((x, y))
            x = x + 25
            pygame.display.flip()


def draw_maze():
    x, y = grid[0]
    visited.append((x, y))
    stack.append((x, y))
    pygame.draw.rect(screen, YELLOW, [x+1, y+1, 23, 23])

    while len(stack) > 0:
        time.sle


def main():
    working = True
    while working:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                working = False
        clock.tick(60)


if __name__ == '__main__':
    draw_grid()
    draw_maze()
    main()
