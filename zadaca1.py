"""
1.Da se napravi programa vo koja korisnikot ke moze da vnese pet elementi, 
da se sobrat site elementi, da se ispecati listata i zbirot na site elementi
"""
lista=[]
zbir=0
for i in range (5):
        element=int(input("Vnesete element: "))
        lista.append(element)
        zbir=zbir+element
print("Ja vnesovte listata:{}".format(lista))
print("Zbirot na elementite e: {}".format(zbir))