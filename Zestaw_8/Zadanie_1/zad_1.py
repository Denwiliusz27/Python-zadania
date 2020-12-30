import json


def create_graph():
    with open('przystanki.json', "r", encoding='utf-8') as read_file:
        przystanki = json.load(read_file)

    with open('tramwaje.json', "r", encoding='utf-8') as read_file:
        tramwaje = json.load(read_file)

    ilosc_linii = len(tramwaje["tramwaje"])

    #for i in tramwaje["tramwaje"][0]["tprzystanki"]:
     #   print(i["name"])



    graph = dict()
    #for i in przystanki["przystanki"]:
        #graph[i] = list()



    for i in range(ilosc_linii):  # ilosc_linii
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
            elif n == len(lista_przystankow)-1:
                if not (lista_przystankow[n-1], 1) in graph[lista_przystankow[n]]:
                    graph[lista_przystankow[n]].append((lista_przystankow[n-1], 1))
            else:
                if not (lista_przystankow[n-1], 1) in graph[lista_przystankow[n]]:
                    graph[lista_przystankow[n]].append((lista_przystankow[n-1], 1))
                if not (lista_przystankow[n+1], 1) in graph[lista_przystankow[n]]:
                    graph[lista_przystankow[n]].append((lista_przystankow[n+1], 1))


    for i in graph.items():
        print(i)

    #for n in graph:
        #print(n + ":" + graph[n])

     #  for j in range(ilosc_linii):
        #    tprzystanki = tramwaje["tramwaje"][j]["tprzystanki"]
         #   for n in tprzystanki:
            #    if n["name"] == ""

         #   for n in tprzystanki:
           #     print(n)

    # print(tramwaje["tramwaje"][0]["name"])

   # graph["Agatowa"].append(("plac", 1))
    #graph["Agatowa"].append(("rondo", 1))

   # print(graph["Agatowa"])




if __name__ == '__main__':
    main()
