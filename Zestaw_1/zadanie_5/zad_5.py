def main():
    sekw_1 = ["kaja", 42.78, True, "maja",[13.2, "ela"], 25, 'a', 25]
    sekw_2 = [False, 'a', 34.22, 25, "maja", 65.11, 'a', ["ela", 13.2]]

    print("\nDwie listy:")
    print(sekw_1)
    print(sekw_2)

    czesc_wspolna = list()
    suma = list()

    for i in sekw_1:
        if i in sekw_2:
            if i not in czesc_wspolna:
                czesc_wspolna.append(i)
        if i not in suma:
            suma.append(i)

    for j in sekw_2:
        if j not in suma:
            suma.append(j)

    print("\nCzesc wspolna :")
    print(czesc_wspolna)

    print("\nSuma wszystkich elementow: ")
    print(suma)

if __name__ == '__main__':
    main()