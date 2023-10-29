#funkcija uredi_seznam naredi nov seznam, v katerega elemente prvotnega seznama, ki se dvakrat zapored ponovijo, napiše enkrat, 
#elemente, ki se trikrat ali štirikrat zapored ponovijo, napiše dvakrat, elemente, ki se samo enkrat, pa pusti pri miru. 

def uredi_seznam(seznam):
    nov_seznam = []
    zaporedne_pojavitve = 1

    for i in range(1, len(seznam)):
        if seznam[i] == seznam[i-1]:
            zaporedne_pojavitve += 1
        else:
            if zaporedne_pojavitve == 1:
                nov_seznam.append(seznam[i-1])
            elif zaporedne_pojavitve in [2, 3, 4]:
                nov_seznam.extend([seznam[i-1]] * 2)
            else:
                nov_seznam.extend([seznam[i-1]])

            zaporedne_pojavitve = 1

    # Dodaj zadnji element
    if zaporedne_pojavitve == 1:
        nov_seznam.append(seznam[-1])
    elif zaporedne_pojavitve in [2, 3, 4]:
        nov_seznam.extend([seznam[-1]] * 2)
    else:
        nov_seznam.extend([seznam[-1]])

    return nov_seznam


#Funkcija, ki mi iz členov seznama, ki vsebuje podatek tipa npr. 3168 ccm, 184 kW / 250 KM izloči samo 250 KM.
def poberi_KM(sez):
    for i in range(len(sez)):
        if '/' in sez[i]:
            sez[i] = sez[i][(-6):]
        if sez[i][0] == ' ':
            sez[i] = sez[i][1:]

#Funkcija, ki pretvori elemente seznama, ki so v kW, v KM (1 kW = 1.341 KM) in zaokroži na najbližje celo število
def pretvorjeno_v_KM(sez):
    for i in range(len(sez)):
        if sez[i][(-2):] == 'kW':
            sez[i] = sez[i][:(-2)]
            sez[i] = str(round(int(sez[i]) * 1.341)) + ' KM'

#Funkcija, ki mi naredi seznam, v katerem so indeksi, na katerih se nahaja element a v seznamu sez
def na_katerih_indeksih_se_nahaja(sez, a):
    i = 0
    sez_indeksov = []
    for el in sez:
        if el == a:
            sez_indeksov.append(i)
        i += 1
    return sez_indeksov

