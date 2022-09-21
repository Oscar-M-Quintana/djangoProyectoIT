archivo = open("aeropuertos.csv", encoding="utf8")
id = 0
diccionario = {}

for datos in archivo:
    id += 1
    lista = datos.split(sep=",")
    diccionario[id] = lista[1:4]
for i in diccionario:
    lista2 = diccionario[i]
    print(lista2[0].strip('"'))
    print(lista2[1])
    print(lista2[2])
