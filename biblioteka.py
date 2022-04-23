"""
a se napravi programa koja bi bila za potrebite na nekoja biblioteka, vo programata da ima moznosti da se vnesuvaat novi knigi, 
da se zaclenuvaat novi clenovi, da se pozajmuvaat knigi, da se vrakjaat knigi.<br>
Podatoci za knigite koi ke treba da se cuvaat: Naslov, avtor, zanr, kolicina<br>
Podatoci za sekoj clen koi ke treba da se cuvaat: Ime i prezime, email, telefonski broj, 
broj na clenska kniska, dali ima zemeno kniga. <br>
Clen koj ima zemeno kniga **ne moze** da zeme druga kniga

*probajte vo razlicni fajlovi "knigi.json", "clenovi.json" da gi cuvate podatocite
"""
def knigi ():
    kniga = input ("Vnesete kniga: ") 
    x[kniga]={}
    x[kniga]['Avtor']=input("Vnesete Avtor na kniga: ")
    x[kniga]['Zarn']=input("Vnesete Zarn na kniga: ")
    x[kniga]['Kolicina']=int(input("Vnesete kolicina: ")) 
    return x

def clenovi():
    brclen = int(input ("Vnesete broj na clenska knishka: "))
    y[brclen]={}
    y[brclen]['ImePrezime']=input("Vnesete nov clen Ime i Prezime: ")
    y[brclen]['email']=input("Vnesete email: ")
    y[brclen]['telefon']=input("Vnesete telefonski broj: ")
    y[brclen]['ZemenoKniga']=int(input("Vnesete dali clenot ima zemeno kniga 1/0: "))
    return y


def PozajmiKniga (x,y):
    i='D'
    p=0
    magacinknigi=x
    magacinclenovi=y
    while i=='D':
        broj=int(input("Vnesete broj na clenska knishka "))
        r=y[broj]['ZemenoKniga']
        if r==1:
            print("Clenot ne moze da zeme vtora kniga")
            i=0
        else:
            print("Clenot moze da zeme kniga ")
            magacinclenovi[broj]['ZemenoKniga']=1
            k=input("Vnesete koja kniga kje ja zeme clenot: ")
            magacinknigi[k]['Kolicina']=x[k]['Kolicina']-1
            p=magacinknigi[k]['Kolicina']
            i=0
            clen=y
            print(clen)
    return magacinknigi


x={}
y={}
magacinknigi={}
magacinclenovi={}

r=input("Dali sakate da vnesete novi Knigi D/N: ")
while r=='D':
    s1=knigi()
    r=input("Dali sakate da prodolzite vo vnesuvanje novi knigi D/N: ")
print(s1)
h=input("Dali sakate da vnesete novi clenovi D/N: ")
while h=='D':
    s2=clenovi()
    h=input("Dali sakate da prodolzite vo vnesuvanje novi clenovi D/N: ")
print(s2)
g=input("Dali dakate da pozajmite kniga D/N: ")
if g=='D':
    s3=PozajmiKniga(x,y)
print("Vo bibliotekata gi ima slednite kolicini na knigi{}".format(s3))
