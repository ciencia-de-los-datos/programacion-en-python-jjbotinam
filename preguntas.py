"""
Laboratorio de Programación Básica en Python para Manejo de Datos
-----------------------------------------------------------------------------------------

Este archivo contiene las preguntas que se van a realizar en el laboratorio.

No puede utilizar pandas, numpy o scipy. Se debe utilizar solo las funciones de python
básicas.

Utilice el archivo `data.csv` para resolver las preguntas.


"""

with open("data.csv", "r") as file:
    data = file.readlines()

# Limpieza
data = [line.replace("\n", "") for line in data]

# Conversión de los strings a listas
data = [line.split("\t") for line in data]


lst = []
with open("data.csv") as f:
    lines = f.readlines()
    for i in lines:
        lst.append(i.replace("\n", ""))

def pregunta_01():
    """
    Retorne la suma de la segunda columna.

    Rta/
    214

    """
    x = 0
    for i in range(0, len(data)):
        x += int(data[i][1])

    return x


def pregunta_02():
    """
    Retorne la cantidad de registros por cada letra de la primera columna como la lista
    de tuplas (letra, cantidad), ordendas alfabéticamente.

    Rta/
    [
        ("A", 8),
        ("B", 7),
        ("C", 5),
        ("D", 6),
        ("E", 14),
    ]

    """
    list_all_letters = []
    for i in range(len(data)):
        list_all_letters.append(data[i][0])

    list_letters = list(dict.fromkeys(list_all_letters))
    list_letters = [i.split("\t")[0] for i in list_letters]
    list_letters.sort()

    answer = []
    for i in range(len(list_letters)):
        answer.append((list_letters[i], list_all_letters.count(list_letters[i])))

    return answer


def pregunta_03():
    """
    Retorne la suma de la columna 2 por cada letra de la primera columna como una lista
    de tuplas (letra, suma) ordendas alfabeticamente.

    Rta/
    [
        ("A", 53),
        ("B", 36),
        ("C", 27),
        ("D", 31),
        ("E", 67),
    ]

    """

    column1 = []
    for i in range(len(data)):
        column1.append(data[i][0])

    column2 = []
    for i in range(len(data)):
        column2.append(data[i][1])

    rr = []
    [rr.append(j) for j in column1 if j not in rr]
    rr.sort()
    dc = {key: 0 for key in rr}
    cc = 0
    for i in column1:
        u = column2[cc]
        a = int(u) + int(dc.get(i))
        dc[i] = a
        cc = cc + 1
    answer = list(dc.items())
    return answer


def pregunta_04():
    """
    La columna 3 contiene una fecha en formato `YYYY-MM-DD`. Retorne la cantidad de
    registros por cada mes, tal como se muestra a continuación.

    Rta/
    [
        ("01", 3),
        ("02", 4),
        ("03", 2),
        ("04", 4),
        ("05", 3),
        ("06", 3),
        ("07", 5),
        ("08", 6),
        ("09", 3),
        ("10", 2),
        ("11", 2),
        ("12", 3),
    ]

    """

    aux1 = []
    aux2 = []
    aux1 = [i.split("\t")[2] for i in lst]
    aux2 = [i.split("-")[1] for i in aux1]
    rr = []
    [rr.append(j) for j in aux2 if j not in rr]
    rr.sort()
    dc = {key: 0 for key in rr}
    for i in aux2:
        a = int(dc.get(i))+1
        dc[i] = a
    dct = list(dc.items())
    return dct

def pregunta_05():
    """
    Retorne una lista de tuplas con el valor maximo y minimo de la columna 2 por cada
    letra de la columa 1.

    Rta/
    [
        ("A", 9, 2),
        ("B", 9, 1),
        ("C", 9, 0),
        ("D", 8, 3),
        ("E", 9, 1),
    ]

    """

    ltr = [i.split("\t")[0] for i in lst]
    num = [i.split("\t")[1] for i in lst]
    k = []
    [k.append(i) for i in ltr if i not in k]
    k.sort()
    dc = {key:[] for key in k}
    c = 0
    lista_final = []
    for i in ltr:
        dc[i].append(num[c])
        c += 1
    for i in k:
        a = (i,int(max(dc[i])),int(min(dc[i])))
        lista_final.append(a)
    return lista_final



def pregunta_06():
    """
    La columna 5 codifica un diccionario donde cada cadena de tres letras corresponde a
    una clave y el valor despues del caracter `:` corresponde al valor asociado a la
    clave. Por cada clave, obtenga el valor asociado mas pequeño y el valor asociado mas
    grande computados sobre todo el archivo.

    Rta/
    [
        ("aaa", 1, 9),
        ("bbb", 1, 9),
        ("ccc", 1, 10),
        ("ddd", 0, 9),
        ("eee", 1, 7),
        ("fff", 0, 9),
        ("ggg", 3, 10),
        ("hhh", 0, 9),
        ("iii", 0, 9),
        ("jjj", 5, 17),
    ]

    """

    dicC = [i.split("\t")[4] for i in lst]
    dicC = [i.split(",") for i in dicC]
    g = []
    for i in dicC:
        g.extend(i)
    dicC = [i.split(":") for i in g]
    g = []
    for i in dicC:
        g.extend(i)
    a = []
    c = 0
    for i in g:
        if c%2 == 0:
            a.append(i)
        c += 1
    aL = []
    [aL.append(j) for j in a if j not in aL]
    aL.sort()
    dc = {k:[] for k in aL}
    for i in dicC:
        dc[i[0]].append(int(i[1]))
    lista_final = []
    for i in aL:
        a = (i, min(dc[i]),max(dc[i]))
        lista_final.append(a)

    return lista_final


def pregunta_07():
    """
    Retorne una lista de tuplas que asocien las columnas 0 y 1. Cada tupla contiene un
    valor posible de la columna 2 y una lista con todas las letras asociadas (columna 1)
    a dicho valor de la columna 2.

    Rta/
    [
        (0, ["C"]),
        (1, ["E", "B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E", "E", "D"]),
        (4, ["E", "B"]),
        (5, ["B", "C", "D", "D", "E", "E", "E"]),
        (6, ["C", "E", "A", "B"]),
        (7, ["A", "C", "E", "D"]),
        (8, ["E", "D", "E", "A", "B"]),
        (9, ["A", "B", "E", "A", "A", "C"]),
    ]

    """

    ltr = [i.split("\t")[0] for i in lst]
    num = [i.split("\t")[1] for i in lst]
    t = []
    [t.append(int(i)) for i in num if i not in t]
    numx = []
    [numx.append(int(i)) for i in num if i not in numx]
    numx.sort()
    dc = {k:[] for k in numx}
    c = 0
    for i in t:
        int(i)
        dc[i].append(ltr[c])
        c += 1
    dev = list(dc.items())
    return dev


def pregunta_08():
    """
    Genere una lista de tuplas, donde el primer elemento de cada tupla contiene  el valor
    de la segunda columna; la segunda parte de la tupla es una lista con las letras
    (ordenadas y sin repetir letra) de la primera  columna que aparecen asociadas a dicho
    valor de la segunda columna.

    Rta/
    [
        (0, ["C"]),
        (1, ["B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E"]),
        (4, ["B", "E"]),
        (5, ["B", "C", "D", "E"]),
        (6, ["A", "B", "C", "E"]),
        (7, ["A", "C", "D", "E"]),
        (8, ["A", "B", "D", "E"]),
        (9, ["A", "B", "C", "E"]),
    ]

    """
    ltr = [i.split("\t")[0] for i in lst]
    num = [i.split("\t")[1] for i in lst]
    h = []
    [h.append(int(i)) for i in num if i not in h]
    numx = []
    [numx.append(i) for i in h if i not in numx]
    numx.sort()
    lo = []
    [lo.append(i) for i in numx if i not in lo]
    dc = {k:[] for k in lo}
    c = 0
    for i in h:
        dc[i].append(ltr[c])
        c += 1
    for i in lo:
        j = list(dc[i])
        u = []
        [u.append(p) for p in j if p not in u]
        u.sort()
        dc[i] = u
    dev = list(dc.items())
    return dev


def pregunta_09():
    """
    Retorne un diccionario que contenga la cantidad de registros en que aparece cada
    clave de la columna 5.

    Rta/
    {
        "aaa": 13,
        "bbb": 16,
        "ccc": 23,
        "ddd": 23,
        "eee": 15,
        "fff": 20,
        "ggg": 13,
        "hhh": 16,
        "iii": 18,
        "jjj": 18,
    }

    """
    rg = [i.split("\t")[4] for i in lst]
    rg = [i.split(",") for i in rg]
    rgf = []
    [rgf.extend(i) for i in rg]
    rg = [i.split(":") for i in rgf]
    lista_codigos = []
    for i in rg:
        lista_codigos.append(i[0])
    R = []
    [R.append(i) for i in lista_codigos if i not in R]
    R.sort()
    ds = {key:0 for key in R}
    for i in R:
        a = lista_codigos.count(i)
        ds[i] = a
    return(ds)


def pregunta_10():
    """
    Retorne una lista de tuplas contengan por cada tupla, la letra de la columna 1 y la
    cantidad de elementos de las columnas 4 y 5.

    Rta/
    [
        ("E", 3, 5),
        ("A", 3, 4),
        ("B", 4, 4),
        ...
        ("C", 4, 3),
        ("E", 2, 3),
        ("E", 3, 3),
    ]

    """
    ltr = [i.split("\t")[0] for i in lst] 
    rg = [i.split("\t")[3] for i in lst]
    rg = [i.replace(",","") for i in rg] 
    dis = [i.split("\t")[4] for i in lst]
    dis = [i.split(",") for i in dis] 
    c = 0
    listaF = []
    for i in ltr:
        a = (i,(len(rg[c])),(len(dis[c])))
        listaF.append(a)
        c += 1
    return(listaF)


def pregunta_11():
    """
    Retorne un diccionario que contengan la suma de la columna 2 para cada letra de la
    columna 4, ordenadas alfabeticamente.

    Rta/
    {
        "a": 122,
        "b": 49,
        "c": 91,
        "d": 73,
        "e": 86,
        "f": 134,
        "g": 35,
    }


    """
    cd = [i.split("\t")[3] for i in lst]
    cd = [i.split(",") for i in cd]
    nm = [i.split("\t")[1] for i in lst]
    ids = []
    for i in cd:
        ids.extend(i)
    idd = []
    [idd.append(i) for i in ids if i not in idd]
    idd.sort()
    ids = {key: 0 for key in idd}
    c = 0
    for i in cd:
        a = nm[c]
        for j in i:
            suma_aux = int(a) + int(ids.get(j))
            ids[j] = suma_aux
        c += 1
    return ids


def pregunta_12():
    """
    Genere un diccionario que contengan como clave la columna 1 y como valor la suma de
    los valores de la columna 5 sobre todo el archivo.

    Rta/
    {
        'A': 177,
        'B': 187,
        'C': 114,
        'D': 136,
        'E': 324
    }

    """

    ID = [i.split("\t")[0] for i in lst]
    ct = [i.split("\t")[4] for i in lst]
    IDi = []
    [IDi.append(i) for i in ID if i not in IDi]
    IDi.sort()
    dc = {key:0 for key in IDi}
    pos = 0
    for i in ct:
        u = i.split(",")
        c1 = 0
        for j in u:
            h = j.split(":")
            c1 = c1 + int(h[1])    
        ky = ID[pos]
        auxiliar_de_suma = c1 + int(dc.get(ky))
        dc[ky] = auxiliar_de_suma
        pos = pos + 1
    return dc
