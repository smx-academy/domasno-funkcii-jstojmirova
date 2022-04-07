"""
Da se napravi programa vo koja korisnikot ke vnese 5 broevi vo razlicni keys, 
da se najde prosekot na tie broevi
"""
broevi={}
broj_eden = int(input ("Vnesete go prviot broj: "))
broevi.update({"broj_eden":broj_eden})
broj_dva=int(input("Vneseto go vtoriot broj: "))
broevi.update({"broj_dva":broj_dva})
broj_tri=int(input("vnesto go tretiot broj: "))
broevi.update({"broj_tri":broj_tri})
broj_cetiri=int(input("vnesto go cetvrtiot broj: "))
broevi.update({"broj_cetiri":broj_cetiri})
broj_pet=int(input("vnesto go pettiot broj: "))
broevi.update({"broj_pet":broj_pet})
z=broevi.get("broj_eden")+broevi.get("broj_dva")+broevi.get("broj_tri")+broevi.get("broj_cetiri")+broevi.get("broj_pet")
broevi.update({"zbir":z})
p=broevi.get("zbir")/5
broevi.update({"prosek":p})
print(broevi)