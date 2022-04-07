"""
Da se napravi programa vo koja korisnikot ke moze da vnese nekolku stringovi, 
dokolku ima broevi vo listata, da se dodadat vo druga lista kako integer ili float
"""

lista1=[]  
lista2=[]
n=int(input(" kolku stringovi kje vnesete: "))
for i in range (n):
    element=input("Vnesete string: ")
    try:
        element!=int(element)
        lista1.append(element)
    except ValueError:
        lista2.append(element)
    
print("lista so int elementi: {}".format(lista1))
print("Lista so str elementi {}".format(lista2))