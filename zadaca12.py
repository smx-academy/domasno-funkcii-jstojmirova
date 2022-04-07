"""
Da se napravi programa vo koja korisnikot ke moze vo dictionary da vnese podatoci za odreden ucenik, ime, mesto na ziveenje, uciliste, 
klas. Vo lista vo dictionary so key otceni da moze da se vnesat otceni na ucenikot. Vo key prosek da se zacuva prosekot na ucenikot, 
a vo key uspeh da se zacuva uspehot na ucenikot( ne dovolen, dovolen, dobar, mn dobar, odlicen)
"""
ucenik={}
ime = input ("Vnesete go vahseto ime: ")
ucenik.update({"Ime":ime})
prezime=input("Vneseto go vasheto prezime: ")
ucenik.update({"Prezime":prezime})
mesto_na_ziveenje=input("vnesto mesto na ziveenje: ")
ucenik.update({"mesto_na_ziveenje":mesto_na_ziveenje})
ucilishte=input("vnesto ucilishte: ")
ucenik.update({"ucilishte":ucilishte})
oceni=[]
n=int(input("Vnesete kolku oceni kje vnesete: "))
z=0
for i in range(n):
    ocena=int(input("Vnesete ocena: "))
    z=z+ocena
    oceni.append(ocena)
    ucenik.update({"oceni":oceni})
p=z/n
ucenik.update({"prosek":p})
if p>4.5:
    ucenik.update({"uspeh":"odlichen"})
elif p<4.5 and p>3.5:
    ucenik.update({"uspeh":"mn dobar"})
elif p<3.5 and p>2.5:
    ucenik.update({"uspeh":"dobar"})
elif p>1.5 and p<2.5:
    ucenik.update({"uspeh":"dovolen"})
else:
    ucenik.update({"uspeh":"ne dovolen"})
print(ucenik)