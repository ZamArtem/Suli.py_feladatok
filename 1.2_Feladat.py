kereszt_nev = []
nev = None
while nev != "":
    if len(kereszt_nev) == 3:
        print("Már nincs lehetősége újabb adat bevitelére")
        break
    nev = input("Kérek egy kereszt nevet: ")
    if nev != "":
        kereszt_nev.append(nev)
print(kereszt_nev)