"""
Da se napravi programa vo koja korisnikot ke vnese odreden broj na elementi vo lista 
i da se najde prosekot na broevite koi se vneseni vo listata
"""
lista=[]
lista1=[]  
zbir=0
prosek=0
n=int(input("Vnesete broj na elementi vo listata: "))
for i in range (n):
        element=int(input("Vnesete go {}-ot element vo listata: ".format(i+1)))
        lista.append(element)
        zbir=zbir+element
prosek=zbir/n
print("Prosekot na broevite e: {}".format(prosek))