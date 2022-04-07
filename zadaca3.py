"""
Da se napravi programa vo koja korisnikot ke vnese odreden broj na elementi,
 da se najde najgolemiot i najmaliot broj i da se ispecatat
 """
lista = []
x=int(input("Vnesete broj na elementi vo nizata: "))
for i in range(x):
    broj=int(input("Vnesete element: "))
    lista.append(broj)
print(lista)
najgolem=max(lista)
najmal=min(lista)
print("Najgolem element vo nizata e: {}".format(najgolem))
print("Najmal element vo nizata e: {}".format(najmal))