"""
Da se napravi programa vo koja korisnikot vo dictionary, 
vo razlicni keys ke vnese 2 broevi, ke se izvrsat osnovnite mat. 
operacii i sekoj rezultat ke se zacuva soodvetno vo nov key
"""
broevi={}
broj_eden = int(input ("Vnesete go prviot broj: "))
broevi.update({"broj_eden":broj_eden})
broj_dva=int(input("Vneseto go vtoriot broj: "))
broevi.update({"broj_dva":broj_dva})
z=broevi.get("broj_eden")+broevi.get("broj_dva")
p=broevi.get("broj_eden")*broevi.get("broj_dva")
r=broevi.get("broj_eden")-broevi.get("broj_dva")
d=broevi.get("broj_eden")/broevi.get("broj_dva")
broevi.update({"zbir":z})
broevi.update({"proizvod":p})
broevi.update({"razlika":r})
broevi.update({"delenje":d})
print(broevi)