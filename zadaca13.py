"""
Da se napravi programa vo koja korisnikot ke moze da pravi to-do lista, 
vo dictionary da moze da vnese 3 'zadaci' so keys (todo1, todo2, todo3),
kako podatoci da se dodade nov dictionary vo format("naslovNaZadaca" naslov, prioritet:2), 
prioritetite da moze da gi kazuva korisnikot
"""


ucenik={}
todo1 = input ("Vnesete zadaca1: ")
ucenik.update({"todo1":todo1})
todo2 = input ("Vnesete zadaca2: ")
ucenik.update({"todo2":todo2})
todo3 = input ("Vnesete zadaca3: ")
ucenik.update({"todo3":todo3})
naslovNaZadaca={}
naslov=input("vnesete naslov na zadaca: ")
naslovNaZadaca.update({"naslov":naslov})
prioritet=int(input("Vnesete prioritet na zadaca 1/2/3: "))
naslovNaZadaca.update({"prioritet":prioritet})
ucenik.update({"naslovNaZadaca":naslovNaZadaca})
print(ucenik)