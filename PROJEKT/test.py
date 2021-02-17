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
    cells = {cell(1, 3) : ["ala", "ela"], cell(2, 4) : ["kaja", "kon"], cell(3, 1): "jurek"}

    c = cell(1, 3)

    print(cells[cell(2, 4)])