"""
Da se napravi programa vo koja korisnikot ke moze vo dictionary da vnese licni podatoci za odreden korisnikot,
 ime, prezime, mesto na ziveenje, godina na ragjanje, email. Spored godinata na ragjanje da se odredi kolku godini
  ima i da se zacuva vo key godini, vo key daliPolnoleten da se zacuva dali e maloleten ili polnoleten.
"""
korisnik={}
ime = input ("Vnesete go vahseto ime: ")
korisnik.update({"Ime":ime})
prezime=input("Vneseto go vasheto prezime: ")
korisnik.update({"Prezime":prezime})
mesto_na_ziveenje=input("vnesto mesto na ziveenje: ")
korisnik.update({"mesto_na_ziveenje":mesto_na_ziveenje})
godina_ragjanje=int(input("Vnesete godina na ragjanje:"))
korisnik.update({"godina na ragjanje":godina_ragjanje})
email=input("Vnesete email:")
korisnik.update({"email":email})
g=korisnik.get("godina na ragjanje")
godini=2022-g
korisnik.update({"godini":godini})
if godini>18 or godini==18:
    daliPolnoleten="Polnoleten"
    korisnik.update({"daliPolnoleten":daliPolnoleten})
else:
    daliPolnoleten="maloleten"
    korisnik.update({"daliPolnoleten":daliPolnoleten})
print(korisnik)