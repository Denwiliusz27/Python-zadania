class Bug:
    licznik = 0

    def __init__(self):
        Bug.licznik += 1
        self.identyfikator = Bug.licznik

    def __del__(self):
        print("KONIEC: ")
        Bug.licznik -= 1

    def __str__(self):
        return 'Licznik = {0}, id = {1}'.format(Bug.licznik, self.identyfikator)


def main():
    bugs = []
    for i in range(10):
        bugs.append(Bug())
        print(bugs[-1])
        print("petla")

    for i in range(10):
        print(bugs[-1])


if __name__ == '__main__':
    main()
