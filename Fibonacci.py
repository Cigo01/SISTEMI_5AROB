#MARCO CIGOTTERO 4 A ROB

#Su python le librerie si possono importare in più modi

 #import LIBRERIA
 #LIBRERIA metodo
 #import LIBRERIA as L
 #L.metodo
 #from LIBRERIA import NOME(I)MODULO(I)


from turtle import *

t=Turtle()  #instanzio l'oggetto Turtle
print("Quanti numeri della sequenza vuoi calcolare?")
i=int(input())      #prendo il numero in input
t.begin_poly()      #inizia a disegnare

cnt=0
n1=1
n2=1
n3=0

while(cnt<i):   # per calcolare la sequenza
    n3=n1+n2
    print(n3)
    n1=n2
    n2=n3
    t.forward(n3)   #disegna di N3
    t.left(90)      # gira di 90 gradi
    cnt+=1

t.end_fill()    #smette di disegnare
done()          #rimane su