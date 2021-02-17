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


def compare_cells(cell1, cell2):
    if cell1.x == cell2.x and cell1.y == cell2.y:
        return True
    else:
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
            grid[Cell(x, y)] = []
            x = x + cell_w
            pygame.display.flip()


def draw_up(cell):
    pygame.draw.rect(screen, BLUE, [cell.x + 2, cell.y - cell_w + 2, cell_w - 3, cell_w * 2 - 3])
    up_neighbour = Cell(cell.x, cell.y - cell_w)
    for i in grid.keys():
        if compare_cells(cell, i):
            grid[i].append(up_neighbour)
        if compare_cells(up_neighbour, i):
            grid[i].append(cell)

    #if cell in grid.keys():
     #   print("jest")
    #grid[cell].append()
   # Cell(cell.x, cell.y - cell_w).walls.remove("d")
    pygame.display.flip()


def draw_right(cell):
    pygame.draw.rect(screen, BLUE, [cell.x + 2, cell.y + 2, cell_w * 2 - 3, cell_w - 3])
    right_neighbour = Cell(cell.x + cell_w, cell.y)
    for i in grid.keys():
        if compare_cells(cell, i):
            grid[i].append(right_neighbour)
        if compare_cells(right_neighbour, i):
            grid[i].append(cell)

    #grid[cell].append(Cell(cell.x + cell_w, cell.y))
    #cell.walls.remove('r')
    #Cell(cell.x + cell_w, cell.y).walls.remove("l")
    pygame.display.flip()


def draw_down(cell):
    pygame.draw.rect(screen, BLUE, [cell.x + 2, cell.y + 2, cell_w - 3, cell_w * 2 - 3])
    down_neighbour = Cell(cell.x, cell.y + cell_w)
    for i in grid.keys():
        if compare_cells(cell, i):
            grid[i].append(down_neighbour)
        if compare_cells(down_neighbour, i):
            grid[i].append(cell)

    #grid[cell].append(Cell(cell.x, cell.y + cell_w))
   # cell.walls.remove('d')
    #Cell(cell.x, cell.y + cell_w).walls.remove("u")
    pygame.display.flip()


def draw_left(cell):
    pygame.draw.rect(screen, BLUE, [cell.x - cell_w + 2, cell.y + 2, cell_w * 2 - 3, cell_w - 3])
    left_neighbour = Cell(cell.x - cell_w, cell.y)
    for i in grid.keys():
        if compare_cells(cell, i):
            grid[i].append(left_neighbour)
        if compare_cells(left_neighbour, i):
            grid[i].append(cell)
    #grid[cell].append(Cell(cell.x - cell_w, cell.y))
    #cell.walls.remove('l')
    #Cell(cell.x - cell_w, cell.y).walls.remove("r")
    pygame.display.flip()


def draw_maze(cell_w):
    cell = Cell(list(grid.keys())[0].x, list(grid.keys())[0].y)
    stack.append(cell)

    pygame.draw.rect(screen, BLUE, [cell.x + 2, cell.y + 2, cell_w - 3, cell_w - 3])
    pygame.display.flip()

    while len(stack) > 0:
        visited.append(cell)

        directions = []  # u - up, r - right, d - down, l - left
        time.sleep(0.1)

        if (Cell(cell.x, cell.y - cell_w).if_in_list(visited) is False) and (Cell(cell.x, cell.y - cell_w).if_in_list(list(grid.keys())) is True):
            directions.append("u")
        if (Cell(cell.x + cell_w, cell.y).if_in_list(visited) is False) and (Cell(cell.x + cell_w, cell.y).if_in_list(list(grid.keys())) is True):  # sprawdza sasiada po prawej
            directions.append("r")
        if (Cell(cell.x, cell.y + cell_w).if_in_list(visited) is False) and (Cell(cell.x, cell.y + cell_w).if_in_list(list(grid.keys())) is True):
            directions.append("d")
        if (Cell(cell.x - cell_w, cell.y).if_in_list(visited) is False) and (Cell(cell.x - cell_w, cell.y).if_in_list(list(grid.keys())) is True):
            directions.append("l")

        if len(directions) > 0:
            number = random.randint(0, len(directions) - 1)
            rand_direction = directions[number]

            if rand_direction == "u":
                draw_up(cell)
                cell = Cell(cell.x, cell.y - cell_w)
            elif rand_direction == "r":
                draw_right(cell)
                cell = Cell(cell.x + cell_w, cell.y)
            elif rand_direction == "d":
                draw_down(cell)
                cell = Cell(cell.x, cell.y + cell_w)
            elif rand_direction == "l":
                draw_left(cell)
                cell = Cell(cell.x - cell_w, cell.y)
            stack.append(cell)
        else:
            cell = stack.pop()

        #print("(", cell.x, cell.y, ") : ", len(cell.walls))

    for i in grid.keys():
        print(i.x, i.y, " -> ")
        for j in range(len(grid[i])):
            print(grid[i][j].x, grid[i][j].y)
    print("koniec")


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

    grid = {}
    visited = []
    stack = []

    cell_w = 25
    draw_grid(3, 3, cell_w)
    draw_maze(cell_w)
    main()
