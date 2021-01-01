import json, random


def wyznacz_wierzcholki(graph, a):
    wierzcholki = dict()
    for wierzcholek in graph.keys():
        wierzcholki[wierzcholek] = []
        if wierzcholek != a:
            wierzcholki[wierzcholek].append(999)
        else:
            wierzcholki[wierzcholek].append(0)
        wierzcholki[wierzcholek].append("")

    return wierzcholki


def losowanie_przystankow(graph):
    wierzcholki = list(graph.keys())
    ilosc_p = len(wierzcholki)

    a = wierzcholki[random.randint(0, ilosc_p - 1)]
    b = wierzcholki[random.randint(0, ilosc_p - 1)]
    while b == a:
        b = wierzcholki[random.randint(0, ilosc_p - 1)]

    return a, b


def create_graph(tramwaje):
    ilosc_linii = len(tramwaje["tramwaje"])

    graph = dict()

    for i in range(ilosc_linii):
        tprzystanki = tramwaje["tramwaje"][i]["tprzystanki"]
        lista_przystankow = list()

        for j in tprzystanki:
            if not j["name"] in graph.keys():
                graph[j["name"]] = list()
            lista_przystankow.append(j["name"])

        for n in range(len(lista_przystankow)):
            if n == 0:
                if not (lista_przystankow[1], 1) in graph[lista_przystankow[n]]:
                    graph[lista_przystankow[n]].append((lista_przystankow[1], 1))
            elif n == len(lista_przystankow) - 1:
                if not (lista_przystankow[n - 1], 1) in graph[lista_przystankow[n]]:
                    graph[lista_przystankow[n]].append((lista_przystankow[n - 1], 1))
            else:
                if not (lista_przystankow[n - 1], 1) in graph[lista_przystankow[n]]:
                    graph[lista_przystankow[n]].append((lista_przystankow[n - 1], 1))
                if not (lista_przystankow[n + 1], 1) in graph[lista_przystankow[n]]:
                    graph[lista_przystankow[n]].append((lista_przystankow[n + 1], 1))

    return graph


def create_list_of_vertices(wierzcholki, a):
    w_nieodwiedzone = [a]
    pos_a = 0
    help_list = list()
    jest_a = False

    for i in wierzcholki:
        if i == a:
            help_list.append(i)
            break
        else:
            help_list.append(i)
        pos_a += 1

    for i in wierzcholki:
        if jest_a == False:
            if i == a:
                jest_a = True
        else:
            w_nieodwiedzone.append(i)

    return w_nieodwiedzone, help_list


def print_path(wierzcholki, a, b):
    sciezka = [b]
    temp = b
    while temp != "":
        sciezka.append(wierzcholki[temp][1])
        temp = wierzcholki[temp][1]

    print(a + " --> " + b + " = " + str(wierzcholki[b][0]))
    for j in range(len(sciezka) - 1, 0, -1):
        print(sciezka[j], end=' -> ')
    print(sciezka[0])


def dijkstra(graph, a, b):
    wierzcholki = wyznacz_wierzcholki(graph, a)

    w_nieodwiedzone = set(graph.keys())
    minimum = wierzcholki[a][0]
    w_min = a

    while w_nieodwiedzone.__len__() > 0:
        for w in w_nieodwiedzone:
            if minimum > wierzcholki[w][0] > 0:
                minimum = wierzcholki[w][0]
                w_min = w
        w_nieodwiedzone.remove(w_min)

        for k in graph[w_min]:
            sasiad = k[0]

            if wierzcholki[sasiad][0] > wierzcholki[w_min][0] + 1:
                wierzcholki[sasiad][0] = wierzcholki[w_min][0] + 1
                wierzcholki[sasiad][1] = w_min

        if w_nieodwiedzone.__len__() > 0:
            minimum = wierzcholki[list(w_nieodwiedzone)[0]][0]
            w_min = list(w_nieodwiedzone)[0]

    print("~~~DIJKSTRA~~~")
    print_path(wierzcholki, a, b)

    return wierzcholki[b][0]


def bellman_ford(graph, a, b):
    wierzcholki = wyznacz_wierzcholki(graph, a)
    w_nieodwiedzone = set(graph.keys())
    sasiedzi_do_odwiedzenia = [a]

    while w_nieodwiedzone.__len__() > 0:
        temp = sasiedzi_do_odwiedzenia[0]
        del sasiedzi_do_odwiedzenia[0]
        w_nieodwiedzone.remove(temp)

        for j in graph[temp]:
            sasiad = j[0]

            if (sasiad in w_nieodwiedzone) and not (sasiad in sasiedzi_do_odwiedzenia):
                sasiedzi_do_odwiedzenia.append(sasiad)

            if wierzcholki[sasiad][0] > wierzcholki[temp][0] + 1:
                wierzcholki[sasiad][0] = wierzcholki[temp][0] + 1
                wierzcholki[sasiad][1] = temp

    print("~~~BELLMAN-FORD~~~")
    print_path(wierzcholki, a, b)

    return wierzcholki[b][0]


def floyd_warshall(graph, a, b):
    wierzcholki = [a]

    for i in range(len(graph.keys())):
        temp = wierzcholki[i]
        for j in graph[temp]:
            sasiad = j[0]
            if not (sasiad in wierzcholki):
                wierzcholki.append(sasiad)

    macierz = [[999] * len(wierzcholki) for i in range(len(wierzcholki))]

    # print(graph[wierzcholki[0]][0])
    # print(wierzcholki[1])

    for i in range(len(macierz)):
        # print("i=" + str(i))
        for j in range(len(macierz)):
            # print("j=" + str(j))
            for n in range(len(graph[wierzcholki[i]])):
                if graph[wierzcholki[i]][n][0] == wierzcholki[j]:
                    # print("ustawiam 1")
                    macierz[i][j] = 1
                    macierz[j][i] = 1
        macierz[i][i] = 0

    # print(wierzcholki)
    # print(macierz[1])

    for i in range(len(macierz)):
        for j in range(len(macierz)):
            for n in range(len(macierz)):
                if macierz[i][j] > macierz[i][n] + macierz[n][j]:
                    macierz[i][j] = macierz[i][n] + macierz[n][j]

    pos_b = 0
    for i in range(len(wierzcholki)):
        if wierzcholki[i] == b:
            pos_b = i
            break

    print(macierz[0][pos_b])

def main():
    with open('przystanki.json', "r", encoding='utf-8') as read_file:
        przystanki = json.load(read_file)

    with open('tramwaje.json', "r", encoding='utf-8') as read_file:
        tramwaje = json.load(read_file)

    graph = create_graph(tramwaje)

    a, b = losowanie_przystankow(graph)

    # print("#######################################")
    odl_dijkstra = dijkstra(graph, a, b)

    # print("\n#######################################")
    odl_bellman = bellman_ford(graph, a, b)

    print("\n#######################################")
    floyd_warshall(graph, a, b)

    print("\nDijkstra = " + str(odl_dijkstra))
    print("\nBellman = " + str(odl_bellman))


if __name__ == '__main__':
    main()
