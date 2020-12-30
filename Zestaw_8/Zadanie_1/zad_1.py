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


def main():
    with open('przystanki.json', "r", encoding='utf-8') as read_file:
        przystanki = json.load(read_file)

    with open('tramwaje.json', "r", encoding='utf-8') as read_file:
        tramwaje = json.load(read_file)

    graph = create_graph(tramwaje)

    for i in graph.items():
        print(i)


if __name__ == '__main__':
    main()
