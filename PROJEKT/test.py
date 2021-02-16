class cell:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def in_list(self, lista):
        for i in lista:
            if i.x == self.x and i.y == self.y:
                print("jestem jako ", i.x, i.y)
                break


if __name__ == '__main__':
    cells = [cell(1, 3), cell(2, 4), cell(3, 1)]

    c = cell(1, 3)
    c.in_list(cells)
