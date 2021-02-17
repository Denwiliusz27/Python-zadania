import pygame
import time
import random


class Cell:
    """ Klasa reprezentująca komórkę w labiryncie
        Labirynt składa się z wielu komórek, każda z nich posida współrzędne x i y, będące wartością pikselową,
        oznaczające położenie komórki w oknie
    """

    def __init__(self, x, y):
        """
            Tworzy nową komórkę o podanych wartościach
        :param x: wartość położenia w poziomie
        :param y: wartośc położenia w pionie
        """
        self.x = x
        self.y = y

    def in_list(self, lista):
        """
            Sprawdza czy komórka znajduje się w podanej liście

            :param lista: lista w której szukamy komórki

            :return: True jeśli komórka znajduje się w liście, False w przeciwnym przypadku
        """
        for i in lista:
            if i.x == self.x and i.y == self.y:
                return True
        return False


def compare_cells(cell1, cell2):
    """
        Porównuje dwie komórki (ich współrzędne)

        :param cell1: pierwsza komórka
        :param cell1: druga komórka

        :return: True: jeśli komórki mają te same współrzędne
        :return: False w przeciwnym przypadku
    """
    if cell1.x == cell2.x and cell1.y == cell2.y:
        return True
    else:
        return False


def draw_grid(grid, x_amount, y_amount, cell_w):
    """
        Służy do stworzenia i narysowania w oknie kraty, będącej podstawą do budowy labiryntu

        :param grid: słownik, którego kluczami są komórki, a wartościami listy ich sąsiadów
        :param x_amount: ilość kolumn
        :param y_amount: ilość wierszy
        :param cell_w: szerokość komórki
        :return: wypełniony słownik
    """
    y = 0

    for i in range(0, y_amount):
        x = 25
        y = y + cell_w
        for j in range(0, x_amount):
            pygame.draw.line(screen, WHITE, [x, y], [x + cell_w, y], 3)  # rysuje górną krawędź komórki
            pygame.draw.line(screen, WHITE, [x + cell_w, y], [x + cell_w, y + cell_w], 3)  # rysuje prawą krawędź
            pygame.draw.line(screen, WHITE, [x, y + cell_w], [x + cell_w, y + cell_w], 3)  # rysuje dolną krawędź
            pygame.draw.line(screen, WHITE, [x, y], [x, y + cell_w], 3)  # rysuje lewą krawędź
            pygame.display.flip()

            grid[Cell(x, y)] = []  # tworzy pustą listę sąsiadów dla komórki, będącej kluczem w słowniku
            x = x + cell_w

    return grid


def add_neighbour(grid, cell, neighbour):
    """
        Dla podanej komórki dodaje sąsiada w liście sąsiadów w słowniku

        :param grid: słownik
        :param cell: komórka, będąca kluczem słownika
        :param neighbour: komórka, która zostaje dodana do listy sasiadów komórki cell
    """
    for i in grid.keys():
        if compare_cells(cell, i):
            grid[i].append(neighbour)  # dodaje sąsiada do listy sąsiadów
        if compare_cells(neighbour, i):
            grid[i].append(cell)  # komórka zostaje dodana jako sąsiad jej sąsiada


def draw_up(grid, cell, cell_w):
    """
        Usuwa górną ścianę danej komórki, zaznacza komórkę powyżej odpowiednim kolorem, oznacza obie komórki jako
        wzajemnych sąsiadów
        :param grid: słownik
        :param cell: komórka, której górną krawędź usuwamy
        :param cell_w: szerokość komórki
    """
    up_neighbour = Cell(cell.x, cell.y - cell_w)
    add_neighbour(grid, cell, up_neighbour)

    pygame.draw.rect(screen, BLUE, [cell.x + 2, cell.y - cell_w + 2, cell_w - 3, cell_w * 2 - 3])


def draw_right(grid, cell, cell_w):
    right_neighbour = Cell(cell.x + cell_w, cell.y)
    add_neighbour(grid, cell, right_neighbour)

    pygame.draw.rect(screen, BLUE, [cell.x + 2, cell.y + 2, cell_w * 2 - 3, cell_w - 3])


def draw_down(grid, cell, cell_w):
    down_neighbour = Cell(cell.x, cell.y + cell_w)
    add_neighbour(grid, cell, down_neighbour)

    pygame.draw.rect(screen, BLUE, [cell.x + 2, cell.y + 2, cell_w - 3, cell_w * 2 - 3])


def draw_left(grid, cell, cell_w):
    left_neighbour = Cell(cell.x - cell_w, cell.y)
    add_neighbour(grid, cell, left_neighbour)

    pygame.draw.rect(screen, BLUE, [cell.x - cell_w + 2, cell.y + 2, cell_w * 2 - 3, cell_w - 3])


def draw_path_cell(cell):
    pygame.draw.rect(screen, YELLOW, [cell.x + cell_w / 3, cell.y + cell_w / 3, cell_w / 3, cell_w / 3])
    pygame.display.flip()


def draw_single_cell(cell):
    pygame.draw.rect(screen, BLUE, [cell.x + 2, cell.y + 2, cell_w - 3, cell_w - 3])
    pygame.display.flip()


def draw_creating_cell(cell):
    pygame.draw.rect(screen, RED, [cell.x + 2, cell.y + 2, cell_w - 3, cell_w - 3])
    pygame.display.flip()


def draw_maze(grid, cell_w):
    stack, visited = [], []

    cell = Cell(list(grid.keys())[0].x, list(grid.keys())[0].y)
    stack.append(cell)

    draw_single_cell(cell)
    pygame.display.flip()

    while len(stack) > 0:
        visited.append(cell)

        directions = []  # u - up, r - right, d - down, l - left
        time.sleep(0.05)

        if (Cell(cell.x, cell.y - cell_w).in_list(visited) is False) and (
                Cell(cell.x, cell.y - cell_w).in_list(list(grid.keys())) is True):
            directions.append("u")
        if (Cell(cell.x + cell_w, cell.y).in_list(visited) is False) and (
                Cell(cell.x + cell_w, cell.y).in_list(list(grid.keys())) is True):  # sprawdza sasiada po prawej
            directions.append("r")
        if (Cell(cell.x, cell.y + cell_w).in_list(visited) is False) and (
                Cell(cell.x, cell.y + cell_w).in_list(list(grid.keys())) is True):
            directions.append("d")
        if (Cell(cell.x - cell_w, cell.y).in_list(visited) is False) and (
                Cell(cell.x - cell_w, cell.y).in_list(list(grid.keys())) is True):
            directions.append("l")

        if len(directions) > 0:
            rand_direction = random.choice(directions)

            if rand_direction == "u":
                draw_up(grid, cell, cell_w)
                cell = Cell(cell.x, cell.y - cell_w)
            elif rand_direction == "r":
                draw_right(grid, cell, cell_w)
                cell = Cell(cell.x + cell_w, cell.y)
            elif rand_direction == "d":
                draw_down(grid, cell, cell_w)
                cell = Cell(cell.x, cell.y + cell_w)
            elif rand_direction == "l":
                draw_left(grid, cell, cell_w)
                cell = Cell(cell.x - cell_w, cell.y)
            stack.append(cell)
            time.sleep(0.05)
            draw_creating_cell(cell)
            pygame.display.flip()
        else:
            draw_single_cell(cell)
            time.sleep(0.05)
            cell = stack.pop()
            draw_creating_cell(cell)

    draw_single_cell(cell)
    return grid


def find_path(grid):
    last_nr = len(list(grid.keys()))
    last_cell = list(grid.keys())[last_nr - 1]

    cell = list(grid.keys())[0]
    stack = []
    visited = []

    while not compare_cells(cell, last_cell):
        neighbours = []
        visited.append(cell)
        draw_path_cell(cell)

        for i in grid.keys():
            if compare_cells(cell, i):
                for j in grid[i]:
                    if not j.in_list(visited):
                        neighbours.append(j)
                break

        if len(neighbours) > 0:
            stack.append(cell)
            cell = random.choice(neighbours)
        else:
            time.sleep(0.15)
            draw_single_cell(cell)
            cell = stack.pop()

        time.sleep(0.15)

    draw_path_cell(cell)


def main():
    working = True
    while working:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                working = False
        clock.tick(30)


if __name__ == '__main__':
    RED = (255, 0, 0)
    YELLOW = (255, 255, 0)
    WHITE = (255, 255, 255)
    BLUE = (0, 0, 255)

    x_cells = 15
    y_cells = 15
    cell_w = 25

    pygame.init()
    width = 50 + x_cells * cell_w
    hight = 50 + y_cells * cell_w

    screen = pygame.display.set_mode((width, hight))
    pygame.display.set_caption("Maze generator")
    clock = pygame.time.Clock()

    grid = {}

    grid = draw_grid(grid, x_cells, y_cells, cell_w)
    grid = draw_maze(grid, cell_w)
    find_path(grid)
    main()
