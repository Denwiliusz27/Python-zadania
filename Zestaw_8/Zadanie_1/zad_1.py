import json


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
        print("zostalo nieodwiedzonych: " + str(len(w_nieodwiedzone)))

        #minimum = wierzcholki[list(w_nieodwiedzone)[0]][0]
        #w_min = list(w_nieodwiedzone)[0]
        print("mam wierzcholek " + list(w_nieodwiedzone)[0])
        for w in w_nieodwiedzone:
            print("Badam: " + w + " : " + str(wierzcholki[w][0]))
            if wierzcholki[w][0] < minimum and wierzcholki[w][0] > 0:
                minimum = wierzcholki[w][0]
                print("bede usuwal " + w)
                w_min = w
        w_nieodwiedzone.remove(w_min)  # discard
        print("minimum: " + str(minimum))

        for k in graph[w_min]:
            sasiad = k[0]

            if wierzcholki[sasiad][0] > wierzcholki[w_min][0] + 1:
                wierzcholki[sasiad][0] = wierzcholki[w_min][0] + 1
                wierzcholki[sasiad][1] = w_min
                print("Update: wierz[" + sasiad + "] = " + str(wierzcholki[sasiad][0]))
        print("###############################################")
        if w_nieodwiedzone.__len__() > 0:
            minimum = wierzcholki[list(w_nieodwiedzone)[0]][0]
            w_min = list(w_nieodwiedzone)[0]

    #print(wierzcholki)
    for i in wierzcholki.keys():
        print(i + ": " + str(wierzcholki[i][0]) + ", " + wierzcholki[i][1])
    return wierzcholki[b][0]

'''
    print("A : " + a)
    wierzcholki = list(graph.keys())
    w_policzone = set()  # S
    w_niepoliczone = set(graph.keys())  # Q
    odl = list()  # d
    poprzednik = list()  # p

    nr_a = -1
    for i in range(len(wierzcholki)):
        if a == wierzcholki[i]:
            nr_a = i

    if nr_a == -1:
        print("Brak takiego przystanku")

    for i in range(len(w_niepoliczone)):
        poprzednik.append(-1)
        if i != nr_a:
            odl.append(999)
        else:
            odl.append(0)

    last_value = -1
    minimum = 0
    while w_niepoliczone.__len__() > 0:
        print("#################################################")
        #print("ODLEGLOSCI: ")
        print("W_niepoliczone rozmiar = " + str(w_niepoliczone.__len__()))
        #print(odl)

        #####
        print("minimum: " + str(minimum))

        for i in range(len(odl)):
            if odl[i] == minimum:
                indeks = i
                break

        print("indeks=" + str(indeks))
        u = wierzcholki[indeks]
        w_policzone.add(u)
       # print(w_policzone)
       # print(w_niepoliczone)
        w_niepoliczone.discard(u)
       # print(w_niepoliczone)

        for j in graph[u]:
            sasiad = j[0]
            print("sasiad: " + sasiad)

            for n in range(len(wierzcholki)):
                if wierzcholki[n] == sasiad:
                    indeks_sasiada = n
                    print("ind_sasiada: " + str(indeks_sasiada))

            if sasiad not in w_niepoliczone:
                print("nie w niepolicz")
                break
            elif odl[indeks_sasiada] > odl[indeks] + 1:
                odl[indeks_sasiada] = odl[indeks] + 1
                poprzednik[indeks_sasiada] = indeks
                print("aktualizuje odl" )

        last_value = odl[0]
        for i in odl:
            if i < last_value and i > minimum:
                minimum = i

    return odl
'''

def main():
    with open('przystanki.json', "r", encoding='utf-8') as read_file:
        przystanki = json.load(read_file)

    with open('tramwaje.json', "r", encoding='utf-8') as read_file:
        tramwaje = json.load(read_file)

    graph = create_graph(tramwaje)

    odleglosci = dijkstra(graph, "Miodowa", "Uniwersytet Pedagogiczny")
    print("#######################################")
    print(odleglosci)

# for i in graph.items():
# print(i)


if __name__ == '__main__':
    main()
