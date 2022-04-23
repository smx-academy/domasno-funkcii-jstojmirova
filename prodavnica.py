"""
Da se napravi programa koja bi bila za potrebite vo nekoja prodavnica, vo programata da ima moznosti da se dodavaat novi produkti, i da moze da se prodavaat. Koga korisnikot ke plati da se presmeta dali i kolku kusur ke treba da mu se vrati i da se odzeme od zalihiti vo prodavnicata.<br>
*moja preporaka "magacinot" neka vi bide vo json fajl
"""

def produkti ():
    produkt = input ("Vnesete produkt: ")
    x[produkt]={}
    x[produkt]['kolicina']=int(input("vnesete kolicina na produktot: "))
    x[produkt]['cena']=int(input("Vnesete cena na produktot: "))
        
    return x

def prodazba (x):
    magacin=x
    i='D'
    p=0
    while i=='D':
        produkt=input("Vnesete produkt sto kje go kupite: ")
        y[produkt]={}
        y[produkt]['kolicina']=int(input("vnesete kolicina: "))
        y[produkt]['cena']=magacin[produkt]['cena']
        p1=y[produkt]['kolicina']
        p2=y[produkt]['cena']
        z=p1*p2
        p=p+z
        i=input("Dali sakate da prodolzite so kupuvanje D/N: ")
        m=magacin[produkt]['kolicina']-y[produkt]['kolicina']
        magacin[produkt]['kolicina']=m
    print("Vo magacin imate: {}".format(magacin))
    print("Fiskalna smetka: {}". format(y))
    return p


x={}
y={}
magacin={}

r=input("Vnesete produkti- D, koristite prodazba - N: ")
while r=="D":
    s1=produkti()
    #print(s1)
    r=input("Dali sakate da prodolzite vo vnesuvanje produkti D/N: ")
    if r!="D":
        s2=prodazba(x)
        print(" Vkupno za plakjanje {} ".format(s2))
        pari=int(input("Vnesete pari od kupuvachot: "))
        kusur=pari-s2
        print("Treba da vratite kusur {}".format(kusur))