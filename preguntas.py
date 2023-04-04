"""
Laboratorio de Programación Básica en Python para Manejo de Datos
-----------------------------------------------------------------------------------------

Este archivo contiene las preguntas que se van a realizar en el laboratorio.

No puede utilizar pandas, numpy o scipy. Se debe utilizar solo las funciones de python
básicas.

Utilice el archivo `data.csv` para resolver las preguntas.


"""
lst = []
with open("data.csv") as f:
    lines = f.readlines()
    for i in lines:
        lst.append(i.replace("\n", ""))

def pregunta_01(lst):
   aux = []
   aux = [i.split("\t")[1] for i in lst]
   c = 0
   for i in aux:
       v = int(i)
       c += v
   return c

def pregunta_02(lst):
   aux = []
   aux = [i.split("\t")[0] for i in lst]
   rr = []
   n = []
   res = []
   [rr.append(j) for j in aux if j not in rr]
   rr.sort()
   for i in rr:
       o = aux.count(i)
       n.append(o)
       res.append((i,o))
   return res

def pregunta_03(lst):   
   aux1 =[]
   aux2 = []
   aux1 = [i.split("\t")[0] for i in lst]
   aux2 = [i.split("\t")[1] for i in lst]
   rr = []
   [rr.append(j) for j in aux1 if j not in rr]
   rr.sort()
   dc = {key: 0 for key in rr}
   cc = 0
   for i in aux1:
       u = aux2[cc]
       a = int(u) + int(dc.get(i))
       dc[i] = a
       cc = cc + 1
   dct = list(dc.items())
   return dct

def pregunta_04(lst):
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

def pregunta_05(lst):
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

def pregunta_06(lst):
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

def pregunta_07(lst):
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

def pregunta_08(lst):
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

def pregunta_09(lst):
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

def pregunta_10(lst):
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

def pregunta_11(lst):
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

def pregunta_12(lst):
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
