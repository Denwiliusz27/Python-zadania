import pygame
import time
import random


class Cell:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def if_in_list(self, lista):
        for i in lista:
            if i.x == self.x and i.y == self.y:
                return True
        return False


def draw_grid(x_amount, y_amount, cell_w):
    y = 0
    for i in range(0, y_amount):
        x = 25
        y = y + cell_w
        for j in range(0, x_amount):
            pygame.draw.line(screen, WHITE, [x, y], [x + cell_w, y], 3)  # gorna krawedz komorki
            pygame.draw.line(screen, WHITE, [x + cell_w, y], [x + cell_w, y + cell_w], 3)  # prawa krawedz
            pygame.draw.line(screen, WHITE, [x, y + cell_w], [x + cell_w, y + cell_w], 3)  # dolna krawedz
            pygame.draw.line(screen, WHITE, [x, y], [x, y + cell_w], 3)  # lewa krawedz
            grid.append(Cell(x, y))
            x = x + cell_w
            pygame.display.flip()


def draw_right(x, y):
    pygame.draw.rect(screen, BLUE, [x + 2, y + 2, cell_w, cell_w*2 + 3])
    pygame.display.flip()


def draw_maze(cell_w):
    cell = Cell(grid[0].x, grid[0].y)
    visited.append(cell)
    stack.append(cell)
    pygame.draw.rect(screen, BLUE, [cell.x + 2, cell.y + 2, cell_w - 3, cell_w - 3])
    pygame.display.flip()

    directions = []  # u - up, r - right, d - down, l - left
    while len(stack) > 0:
        if ((cell.x, cell.y - cell_w) not in visited) and ((cell.x, cell.y - cell_w) in grid):
            directions.append("u")
        elif ((cell.x + cell_w, cell.y) not in visited) and ((cell.x + cell_w, cell.y) in grid):  # sprawdza sasiada po prawej
            directions.append("r")
        elif ((cell.x, cell.y + cell_w) not in visited) and ((cell.x, cell.y + cell_w) in grid):
            directions.append("d")
        elif ((cell.x - cell_w, cell.y) not in visited) and ((cell.x - cell_w, cell.y) in grid):
            directions.append("l")

        if len(directions) > 0:
            rand_direction = 


def main():
    working = True
    while working:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                working = False
        clock.tick(60)


if __name__ == '__main__':
    BLACK = (0, 0, 0)
    RED = (255, 0, 0)
    YELLOW = (255, 255, 0)
    WHITE = (255, 255, 255)
    BLUE = (0, 0, 255)

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

    cell_w = 25
    draw_grid(30, 20, cell_w)
    draw_maze(cell_w)
    main()
