import json, random


def losowanie_przystankow(graph):
    wierzcholki = list(graph.keys())
    ilosc_p = len(wierzcholki)

    a = wierzcholki[random.randint(0, ilosc_p - 1)]
    b = wierzcholki[random.randint(0, ilosc_p - 1)]
    if b == a:
        while b != a:
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


def dijkstra(graph, a, b):
    wierzcholki = dict()
    for wierzcholek in graph.keys():
        wierzcholki[wierzcholek] = []
        if wierzcholek != a:
            wierzcholki[wierzcholek].append(999)
            wierzcholki[wierzcholek].append("")
        else:
            wierzcholki[wierzcholek].append(0)
            wierzcholki[wierzcholek].append("")

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

    sciezka = [b]
    temp = b
    while temp != "":
        sciezka.append(wierzcholki[temp][1])
        temp = wierzcholki[temp][1]

    print(a + " --> " + b + " = " + str(wierzcholki[b][0]))
    for j in range(len(sciezka)-1, 0, -1):
        print(sciezka[j], end=" -> ")
    print(sciezka[0])

    return wierzcholki[b][0]


def main():
    with open('przystanki.json', "r", encoding='utf-8') as read_file:
        przystanki = json.load(read_file)

    with open('tramwaje.json', "r", encoding='utf-8') as read_file:
        tramwaje = json.load(read_file)

    graph = create_graph(tramwaje)

    a, b = losowanie_przystankow(graph)

    odleglosc = dijkstra(graph, a, b)
    print("#######################################")
    print("Dijkstra = " + str(odleglosc))


# for i in graph.items():
# print(i)


if __name__ == '__main__':
    main()
