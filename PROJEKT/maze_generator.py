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


def draw_up(cell):
    pygame.draw.rect(screen, BLUE, [cell.x + 2, cell.y - cell_w + 2, cell_w - 3, cell_w * 2 - 3])
    pygame.display.flip()


def draw_right(cell):
    pygame.draw.rect(screen, BLUE, [cell.x + 2, cell.y + 2, cell_w * 2 - 3, cell_w - 3])
    pygame.display.flip()


def draw_down(cell):
    pygame.draw.rect(screen, BLUE, [cell.x + 2, cell.y + 2, cell_w - 3, cell_w * 2 - 3])
    pygame.display.flip()


def draw_left(cell):
    pygame.draw.rect(screen, BLUE, [cell.x - cell_w + 2, cell.y + 2, cell_w * 2 - 3, cell_w - 3])
    pygame.display.flip()


def draw_maze(cell_w):
    cell = Cell(grid[0].x, grid[0].y)
    # visited.append(cell)
    stack.append(cell)
    pygame.draw.rect(screen, BLUE, [cell.x + 2, cell.y + 2, cell_w - 3, cell_w - 3])
    pygame.display.flip()

    while len(stack) > 0:
        visited.append(cell)

        directions = []  # u - up, r - right, d - down, l - left
        time.sleep(0.1)

        if (Cell(cell.x, cell.y - cell_w).if_in_list(visited) is False) and (Cell(cell.x, cell.y - cell_w).if_in_list(grid) is True):
            directions.append("u")
            #print("Dodaje U")
        if (Cell(cell.x + cell_w, cell.y).if_in_list(visited) is False) and (Cell(cell.x + cell_w, cell.y).if_in_list(grid) is True):  # sprawdza sasiada po prawej
            directions.append("r")
            #print("Dodaje R")
        if (Cell(cell.x, cell.y + cell_w).if_in_list(visited) is False) and (Cell(cell.x, cell.y + cell_w).if_in_list(grid) is True):
            directions.append("d")
            #print("Dodaje D")
        if (Cell(cell.x - cell_w, cell.y).if_in_list(visited) is False) and (Cell(cell.x - cell_w, cell.y).if_in_list(grid) is True):
            directions.append("l")
            #print("Dodaje L")

        print("directions ma : ", len(directions))
        if len(directions) > 0:
            number = random.randint(0, len(directions) - 1)
            rand_direction = directions[number]

            if rand_direction == "u":
                print("wybralem U")
                draw_up(cell)
                cell = Cell(cell.x, cell.y - cell_w)
            elif rand_direction == "r":
                print("wybralem R")
                draw_right(cell)
                cell = Cell(cell.x + cell_w, cell.y)
            elif rand_direction == "d":
                print("wybralem D")
                draw_down(cell)
                cell = Cell(cell.x, cell.y + cell_w)
            elif rand_direction == "l":
                print("wybralem L")
                draw_left(cell)
                cell = Cell(cell.x - cell_w, cell.y)

            stack.append(cell)
            #print("new cell: x=", cell.x, " y=", cell.y)

        else:
            cell = stack.pop()


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
    draw_grid(7, 7, cell_w)
    draw_maze(cell_w)
    main()
