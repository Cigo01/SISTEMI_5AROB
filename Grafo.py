#MARCO CIGOTTERO 4 A ROB

#trovo i nodi confinanti in un grafo
m=[[0,1,0,1,0],
   [1,0,1,1,1],
   [0,1,0,1,0],
   [1,1,1,0,0],
   [0,1,0,0,0]]

nodo = -1

for j in m: #scorro i nodi della matrice
    cnt=0
    nodo +=1
    vicini = [] #vettore che conterrà i vicini per ogni nodo
    for k in j: #scorro le liste che indicano i vicini per ogni nodo
        if(k==1):
            vicini.append(cnt)
        cnt +=1

    print("nodo:" + str(nodo) + " = "  + str(vicini))    #stampo i vicini per il nodo esaminato