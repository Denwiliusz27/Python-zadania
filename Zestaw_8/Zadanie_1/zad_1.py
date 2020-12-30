import json


def main():
    with open('przystanki.json', "r", encoding='utf-8') as read_file:
        przystanki = json.load(read_file)

    with open('tramwaje.json', "r", encoding='utf-8') as read_file:
        tramwaje = json.load(read_file)

    ilosc_linii = len(tramwaje["tramwaje"])

    #for i in tramwaje["tramwaje"][0]["tprzystanki"]:
     #   print(i["name"])



    graph = dict()
    for i in przystanki["przystanki"]:
        graph[i] = list()



    for i in range(1):
        tprzystanki = tramwaje["tramwaje"][i]["tprzystanki"]
        lista_przystankow = list()

        for j in tprzystanki:
            lista_przystankow.append(j["name"])

        print(lista_przystankow)


     #  for j in range(ilosc_linii):
        #    tprzystanki = tramwaje["tramwaje"][j]["tprzystanki"]
         #   for n in tprzystanki:
            #    if n["name"] == ""

         #   for n in tprzystanki:
           #     print(n)

    print(tramwaje["tramwaje"][0]["name"])

   # graph["Agatowa"].append(("plac", 1))
    #graph["Agatowa"].append(("rondo", 1))

   # print(graph["Agatowa"])




if __name__ == '__main__':
    main()
