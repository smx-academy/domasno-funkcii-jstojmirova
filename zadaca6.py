"""
Da se napravi programa vo koja korisnikot ke moze da vnese nekolku stringovi vo lista, 
da se ispecatat site elementi koi se podolgi od 3 karakteri
"""
lista=[]
lista1=[]  
lista2=[]
n=int(input(" kolku stringovi kje vnesete: "))
for i in range (n):
    string=input("Vnesete string: ")
    lista.append(string)
    l=len(lista[i])
    if l>3:
        lista1.append(string)
    else:
        lista2.append(string)
print("Stringovi so povekje od 3 karakteri se {}".format(lista1))
print("Stringovi so pomalku od 3 i 3 karakteri se {}".format(lista2))