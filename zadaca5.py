"""
Da se napravi programa vo koja korisnikot ke moze da vnese odreden broj na elementi vo lista, parnite broevi da se soberat, 
ne parnite da se pomnozat. 
Da se ispecati koi se parni, a koi se ne parni zaedno so nivnite rezultati
"""
lista = []
lista1=[]
lista2=[]
z=0
p=1
n=int(input("Vnesete broj na elementi vo listata: "))
for i in range (n):
    element=int(input("Vnesete go {}-ot element vo listata: ".format(i+1)))
    lista.append(element)
    if element%2 == 0:
        lista1.append(element)
        z=z+element
    else:
        lista2.append(element)
        p=p*element
print("Ja vnesovte listata:{}".format(lista))
print("Parni se broevite {}, zbirot na parnite broevi e {}" .format (lista1, z))
print("Neparni se broevite {}, proizvodot na neparnite broevi e {}" .format (lista2,p))
