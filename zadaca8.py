"""
Da se napravi programa vo koja korisnikot ke moze da vnese nekolku elementi vo lista
i da se ispecati sekoj element kolku pati se pojavuva vo listata
"""
lista=[]
n=int(input(" kolku elementi kje vnesete: "))
for i in range (n):
    element=input("Vnesete element: ")
    lista.append(element)
for j in range(n):
    b=lista[j]
    c=lista.count(b)
    print("Brojot {} se pojavuva {} pati".format(b,c))