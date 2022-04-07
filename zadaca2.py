"""
Da se napravi programa vo koja korisnikot ke moze da vnese odreden broj na elementi,
 da se pomnozat site elementi, proizvodot da se podeli so 2 i da se ispecati
"""
lista=[]
lista1=[]  
proizvod=1
pr=0
n=int(input("Vnesete kolku elementi kje vnesete: "))
for i in range (n):
    element=int(input("Vnesete element: "))
    lista.append(element)
    proizvod=proizvod*element
print(proizvod)
pr=proizvod/2
print(pr)