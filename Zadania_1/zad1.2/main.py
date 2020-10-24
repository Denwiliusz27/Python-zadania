def main():
    print("\nWypisuje liczby od 0 do 30, procz tych podzielnych przez 3. Oto one:")

    for i in range(31):
        if not i % 3 == 0:
            print(i, end=" ")

    print()


if __name__ == '__main__':
    main()